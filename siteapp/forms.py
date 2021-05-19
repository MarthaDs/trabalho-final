from django import forms
from django.db import models
from django.db.models import fields
from django.forms import inlineformset_factory
from .models import Candidate, PhysicalCharacteristic, SocialRace, Intelect


class PhysicalCharacteristicForm(forms.ModelForm):

  class Meta:
    model = PhysicalCharacteristic
    fields = '__all__'

class IntelectForm(forms.ModelForm):

  class Meta:
    model = Intelect
    fields = '__all__'

class SocialRaceForm(forms.ModelForm):

  class Meta:
    model = SocialRace
    fields = '__all__'



