from unittest.mock import patch
from django.test import TestCase
from django.test import Client
from django.db.utils import IntegrityError
from .models import Room

class RoomTestCase(TestCase):
    def setUp(self):
        room = Room(
            name="Sala",
            people_count=0,
            max_people_count=10,
            image=None)
        room.save()

    def test_str(self):
        room = Room.objects.get(name="Sala")
        self.assertEqual(str(room), "Sala")

    def test_max_people_constraint(self):
        room = Room.objects.get(name="Sala")
        room.people_count = 11
        with self.assertRaises(IntegrityError):
            room.save()

class PeopleTrackingTestCase(TestCase):
    fixtures = ['example']

    def test_moving_people(self):
        room1 = Room.objects.get(name="Sala1")
        room2 = Room.objects.get(name="Sala2")
        #fixtura ustawia: room1.poeple_count=9, room2.people_count=1
        room1.move_people_to(room2, 2)
        room1.refresh_from_db()
        room2.refresh_from_db()
        self.assertEqual(room1.people_count, 7)
        self.assertEqual(room2.people_count, 3)

class ViewsTestCase(TestCase):
    fixtures = ['example']

    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get('/')
        # self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book a room")

    def test_create_reservation(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(
            '/reserve',
            {'room': 1, 'date': '2022-06-04'}
        )
        self.assertRedirects(response, '/reservations')


class MockRequestsResponse:
    def json(self):
        return\
            {
                "current_condition": [
                    {
                        "FeelsLikeC": "25",
                        "FeelsLikeF": "76",
                        "cloudcover": "100",
                        "humidity": "76",
                        "observation_time": "04:08 PM",
                        "precipMM": "0.2",
                        "pressure": "1019",
                        "temp_C": "22"
		            }
                ]
            }

class WatherTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("requests.get", return_value=MockRequestsResponse())
    def test_temperature_in_warsaw(self, mock_requests_get):
        response = self.client.get('/weather/Warsaw')
        self.assertContains(response, "Temperature is 22")
        self.assertTrue(mock_requests_get.called)
