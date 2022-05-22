from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView
from django.db.utils import IntegrityError

from .models import Reservation
from .forms import ReservationForm, ReservationFrom2

def home(request):
    # request.user.username
    return render(request, 'buildingmanagement/home.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Reservation(
                room=form.cleaned_data["room"],
                date=form.cleaned_data["date"],
                user=request.user
            )
            try:
                reservation.save()
            except IntegrityError as e:
                # TODO: sprawdzenie czy to na pewno ten constraint
                # np. e.args: ('UNIQUE constraint failed: buildingmanagement_reservation.room_id, buildingmanagement_reservation.date',)
                form.add_error("date", "Room already taken")
            else:
                return redirect("reservations")
    else:
        form = ReservationForm()
    return render(request, 'buildingmanagement/reserve.html', {'form': form})

@login_required
def reserve2(request):
    if request.method == "POST":
        form = ReservationFrom2(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)  # nie zapisuje w bazie
            reservation.user = request.user
            reservation.save()
            return redirect("reservations")
    else:
        form = ReservationFrom2()
    return render(request, 'buildingmanagement/reserve.html', {'form': form})

class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
