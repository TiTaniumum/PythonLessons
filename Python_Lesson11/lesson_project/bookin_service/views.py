from django.shortcuts import render
from bookin_service.models import Room
from django.shortcuts import get_object_or_404
from bookin_service.forms import RoomForm
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
    
    return render(request, "bookin_service/create_room.html", {"form":form})