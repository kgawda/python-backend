from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<int:room_id>", views.room, name="room"),
    path("room/add", views.AddRoom.as_view(), name="add_room"),
    path("reserve", views.reserve, name="reserve"),
    path("reserve2", views.reserve2),
    path("reservations", views.ReservationListView.as_view(), name="reservations"),
    path("warnings", views.no_card_warnings, name='no_card_warnings'),
    path("signup", views.signup, name="signup"),
    path("weather/<str:city>", views.WeatherInfo.as_view(), name="weather")
] + static("images/", document_root="images/")
