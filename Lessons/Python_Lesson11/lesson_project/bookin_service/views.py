from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from bookin_service.models import Room
from django.shortcuts import get_object_or_404
from bookin_service.forms import RoomForm
from bookin_service.forms import ConfirmDeleteForm, UserRegistrationForm
from django.db.models import Q, Count, Avg
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
# Create your views here.

# class RoomListView(View):
#     # dispatch()
#     # setup()
#     # as_view()
#     def get(self, request):
#         all_rooms = Room.objects.annotate(bookin_count = Count("booking"))
#         average_price = Room.objects.aggregate(Avg("price"))
#         context = {
#             "rooms": all_rooms,
#             "avg_price": average_price["price__avg"]
#         }
#         return render(request, "bookin_service/room_list.html",context)

class RoomListView(ListView):
    model = Room
    context_object_name = "rooms"
    #template_name:str = "bookin_service/room_list.html"

    def get_queryset(self):
        return self.model.objects.annotate(bookin_count=Count("booking"))
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["avg_price"] = self.model.objects.aggregate(Avg("price"))["price_avg"]
        return context
    
    # def get(self):
    #     queryset = self.get_queryset()
    #     context = self.get_context_data(queryset=queryset)
    #     return render()

class RoomDetailView(DetailView):
    model = Room
    pk_url_kwarg: str = "room_id"

    # def get_object(self, queryset):
    #     return self.get_qeuryset().get(pk=self.object_id)

class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy("room_list")
    template_name: str = "bookin_service/room_form.html"

class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy("room_list")
    template_name: str = "bookin_service/room_form.html"
    pk_url_kwarg: str = "room_id"

class RoomDeleteView(DeleteView):
    model = Room
    template_name: str = "bookin_service/room_form.html"


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

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("room_list")
    else:
        form = UserRegistrationForm()
    return render(request, "bookin_service/register.html", {"form":form})