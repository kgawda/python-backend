from django.db import models
from django.db import transaction
from django.db.models import F, Q
from django.db.models import UniqueConstraint, CheckConstraint
from django.contrib.auth.models import User
from django.conf import settings


class Room(models.Model):
    name = models.CharField(max_length=100)
    people_count = models.PositiveSmallIntegerField(default=0)
    max_people_count = models.PositiveSmallIntegerField(null=False)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(people_count__lte=F('max_people_count')),
                name="people_count_maximum"
            )
        ]
        #Room.objects.filter(people_count__lte=F('max_people_count'))

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
    #user = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ^ takie użycie User zadziała, ale może sprawić kłopoty później
    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#referencing-the-user-model
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    class Meta:
        #unique_together = [["room", "date"]]
        # from django.db.models import UniqueConstraint
        constraints = [
            UniqueConstraint(fields=["room", "date"], name="unique_room_reservation")
        ]
        ordering = ['date']

    def __str__(self):
        return f"{self.room.name}/{self.date}"
