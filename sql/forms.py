from .models import Person, Image
from django.forms import ModelForm
from django import forms


class Subscribe(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = {'id', 'firstname', 'lastname', 'year'}


class ImageForm(ModelForm):

    class Meta:
        model = Image
        fields = ['id', 'image']