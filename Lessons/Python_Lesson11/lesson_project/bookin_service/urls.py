from django.contrib import admin
from bookin_service.views import room_list, room_detail, create_room, update_room, delete_room, register, RoomListView, RoomDetailView
from django.urls import path
# from my_app.views import index

urlpatterns = [
    path("rooms/", RoomListView.as_view(),name = "room_list"),
    path("rooms/<int:room_id>", RoomDetailView.as_view(),name = "room_detail"),
    path("rooms/", room_list, name="room_list"),
    path("rooms/<int:room_id>",room_detail, name="room_detail"),
    path("room_create/", create_room, name="room_create"),
    path("room_update/<int:room_id>", update_room, name="update_room"),
    path("room_delete/<int:room_id>", delete_room, name="room_delete"),
    path("register/",register,name="registration")
]