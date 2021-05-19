from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Candidate, Stereotype
from .forms import PhysicalCharacteristicForm, SocialRaceForm, IntelectForm, StereotypeForm
import random


# Create your views here.

def index(request):
    return render(request, 'siteapp/index.html')

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'siteapp/candidate_list.html', {'candidates': candidates})

def new_candidate(request):
    stereotype = None
    if request.method == "POST":
        form_physical = PhysicalCharacteristicForm(request.POST)
        form_race = SocialRaceForm(request.POST)
        form_intelect = IntelectForm(request.POST)
        if form_physical.is_valid() and form_race.is_valid() and form_intelect.is_valid():
            physical_characteristic = form_physical.save(commit=True)
            race = form_race.save(commit=True)
            intelect = form_intelect.save(commit=True)
            created_date = timezone.now()
            if race.race == 'black':
                stereotype = Stereotype.objects.create(stereotype='inferior_race')
            else:
                stereotype = Stereotype.objects.create(stereotype='superior_race')
            candidate = Candidate.objects.create(physical_characteristic=physical_characteristic,
                intelect=intelect, race=race, created_date=created_date, stereotype=stereotype)
            candidate.save()
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form_physical = PhysicalCharacteristicForm()
        form_race = SocialRaceForm()
        form_intelect = IntelectForm()
    return render(request, 'siteapp/candidate_edit.html', {'form_physical': form_physical,
        'form_race': form_race, 'form_intelect': form_intelect})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    context = {
        'candidate': candidate,
    }

    return render(request, 'siteapp/candidate_detail.html', context)