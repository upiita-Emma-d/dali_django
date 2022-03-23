from django import forms
from django.forms import ModelForm
from django import forms
from ProcesadorImg.models import ImagenBase

class FormImagen(ModelForm):
    class Meta:
        model = ImagenBase
        fields = ('title','image')