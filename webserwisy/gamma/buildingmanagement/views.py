from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.db.utils import IntegrityError

from .models import Reservation, Room
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
    # objects = Reservation.objects.all()
    # context = {'objects': objects}
    # return render(request, 'buildingmanagement/reservation_list.html', context)

def room(request, room_id):
    #room = get_object_or_404(Room, id=room_id)
    room = Room.objects.filter(id=room_id).prefetch_related('projector', 'accesscards').first()
    # Dzięki prefetch_related zaoszczędzimy późniejszych zapytań do bazy

    # skrót do utorzenia nowej karty, zapisania w bazie i dodania do relacji:
    # card = room.accesscards.create(owner=request.user)

    reserved_days = room.get_reserved_days(month=5)
    # jak sprawdzić czy sala ma rzutnik? tak: hasattr(room, "projector")

    return render(
        request,
        'buildingmanagement/room.html',
        {
            'room': room,
            'reserved_days': reserved_days,
            'days_in_month': range(1, 32)
        }
    )

# Rzutniki w salach, które mają przynajmniej jedną rezerwację w maju:
# Projector.objects.filter(room__reservation__date__month=5).distinct()


def no_card_warnings(request):
    today = datetime.today()
    after30 = today + timedelta(days=30)
    warning_rooms = Room.objects.filter(
        reservation__date__gte=today,
        reservation__date__lt=after30,
        reservation__user=request.user
    ).exclude(
        accesscards__owner=request.user
    ).distinct()

    return render(request, 'buildingmanagement/warnings.html', {'warning_rooms': warning_rooms})


