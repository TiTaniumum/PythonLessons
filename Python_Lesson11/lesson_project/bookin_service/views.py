from django.shortcuts import render, redirect
from bookin_service.models import Room
from django.shortcuts import get_object_or_404
from bookin_service.forms import RoomForm
from bookin_service.forms import ConfirmDeleteForm
from django.db.models import Q, Count
# Create your views here.

def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "bookin_service/room_list.html",context)

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, "bookin_service/room_detail.html",{"room":room})

def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm()
    
    return render(request, "bookin_service/room_create.html", {"form":form})

def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(instance=room)
    return render(request,"bookin_service/room_form.html", {"form": form})

def delete_room(request,room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == "POST":
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirm"]:
            room.delete()
            return redirect("room_list")
    else:
        form = ConfirmDeleteForm()
    return render(request, "bookin_service/room_create.html",{"form": form})

