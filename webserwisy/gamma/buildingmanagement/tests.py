from django.test import TestCase
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
