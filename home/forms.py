from django.forms import ModelForm
from django import forms
from home.models import Data

class FormData(ModelForm):
    class Meta :
        model = Data
        fields = '__all__'