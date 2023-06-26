from django import forms
from .models import Portfolio
from .models import Message

class editForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "desc", "img"]

class messageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "message"]