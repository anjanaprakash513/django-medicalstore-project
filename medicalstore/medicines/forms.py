from django import forms
from .models import medList

class medForm(forms.ModelForm):
  class Meta:
    model = medList
    fields = '__all__'