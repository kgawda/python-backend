from django.db import models
from django.db import transaction
from django.db.models import F


class Room(models.Model):
    name = models.CharField(max_length=100)
    people_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    @transaction.atomic
    def move_people_to(self, other_room, count=1):
        #### Nie odporne na równoległy zapis w bazie
        # self.people_count -= count
        # self.save()
        # other_room.people_count += count
        # other_room.save()

        #Room.objects.filter(id=self.id).update(people_count=F("people_count") - count)
        #Room.objects.filter(id=other_room.id).update(people_count=F("people_count") + count)
        # albo:
        # self.people_count = F("people_count") - count
        # self.save()
        # other_room.people_count = F("people_count") + count
        # other_room.save()
        # # ale uwaga: powysze pozostawia obiekt F w self.people_coun,
        # # więc kolejny self.save znów mniejszy wartość.
        # # Dopiero self.refresh_from_db() wyczyści nam to pole

        ### inne podejście do radzenia sobie z równoległymi zapisami do bazy (blokuje do końca transakcji)
        Room.objects.filter(id=self.id).select_for_update()
        Room.objects.filter(id=other_room.id).select_for_update()
        self.people_count -= count
        self.save()
        other_room.people_count += count
        other_room.save()

        ### inny sposób użycia transakcji:
        # with transaction.atomic():
        #     self.people_count -= count
        #     self.save()
        #     other_room.people_count += count
        #     other_room.save()


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.room.name}/{self.date}"
