from django.contrib import admin
from buildingmanagement.models import Room, Reservation, Projector, AccessCard

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Projector)
admin.site.register(AccessCard)