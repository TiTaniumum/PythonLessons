from django import forms
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        widgets = {
            "available": forms.CheckboxInput(attrs = {"class": "form-check"})
        }
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 5:
            raise forms.ValidationError("Название комнаты должно содуржать не менее пяти символов")
        return name

class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Вы уверены, что хотите удалить комнату?")