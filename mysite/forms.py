from django import forms

from .models import MyModel


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["name", "email", "phone", "message", ]
        labels = {'name': 'Name', 'email': 'Email', 'phone': 'Phone', 'message': 'Message', }
