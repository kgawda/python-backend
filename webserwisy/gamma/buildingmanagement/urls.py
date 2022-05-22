from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reserve", views.reserve, name="reserve"),
    path("reserve2", views.reserve2),
    path("reservations", views.ReservationListView.as_view(), name="reservations"),
    path("signup", views.signup, name="signup")
]