from django.contrib import admin
from bookin_service.views import room_list, room_detail
from django.urls import path
# from my_app.views import index

urlpatterns = [
    path("rooms/", room_list, name="room_list"),
    path("rooms/<int:room_id>",room_detail, name="room_detail")
]
