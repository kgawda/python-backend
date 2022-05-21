from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reservations", views.ReservationListView.as_view(), name="reservations"),
    path("signup", views.signup, name="signup")
]