from django import forms
from django.db import models
from django.db.models import fields
from django.forms import inlineformset_factory
from .models import Candidate, PhysicalCharacteristic, SocialRace, Intelect, Stereotype


class PhysicalCharacteristicForm(forms.ModelForm):

  def __init__(self, *args, **kargs):
    super(PhysicalCharacteristicForm, self).__init__(*args, **kargs)

  class Meta:
    model = PhysicalCharacteristic
    fields = '__all__'

class IntelectForm(forms.ModelForm):
  def __init__(self, *args, **kargs):
    super(IntelectForm, self).__init__(*args, **kargs)
  
  class Meta:
    model = Intelect
    fields = '__all__'

class SocialRaceForm(forms.ModelForm):
  def __init__(self, *args, **kargs):
    super(SocialRaceForm, self).__init__(*args, **kargs)

  class Meta:
    model = SocialRace
    fields = '__all__'

class StereotypeForm(forms.ModelForm):
  def __init__(self, *args, **kargs):
    super(StereotypeForm, self).__init__(*args, **kargs)

  class Meta:
    model = Stereotype
    fields = '__all__'


