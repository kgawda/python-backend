import datetime

from django import forms
from .models import Room, Reservation


class ReservationForm(forms.Form):
    room = forms.ModelChoiceField(Room.objects)
    date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.SelectDateWidget(empty_label="Nothing")
    )

class ReservationFrom2(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["room", "date"]
        widgets = {
            "date": forms.SelectDateWidget(empty_label="Nothing")
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = []
