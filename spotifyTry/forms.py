from django.forms import ModelForm
from .models import Persona


class FormPersona(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
