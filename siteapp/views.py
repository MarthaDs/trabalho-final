from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Candidate
from .forms import PhysicalCharacteristicForm, SocialRaceForm, IntelectForm


# Create your views here.
def candidate_list(request):
    candidates = Candidate.objects.filter(created_date=timezone.now()).order_by('created_date')
    return render(request, 'siteapp/candidate_list.html', {'candidates': candidates})

def new_candidate(request):
    if request.method == "POST":
        form_physical = PhysicalCharacteristicForm(request.POST)
        form_race = SocialRaceForm(request.POST)
        form_intelect = IntelectForm(request.POST)
        if form_physical.is_valid() and form_race.is_valid() and form_intelect.is_valid():
            candidate = Candidate.objects.create()
            candidate.created_date = timezone.now()
            candidate.race = form_race.save(commit=False)
            candidate.physical_characteristic = form_physical.save(commit=False)
            candidate.intelect = form_intelect.save(commit=False)
            candidate.save()
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form_physical = PhysicalCharacteristicForm()
        form_race = SocialRaceForm()
        form_intelect = IntelectForm()
    return render(request, 'siteapp/candidate_edit.html', {'form_physical': form_physical,
        'form_race': form_race, 'form_intelect': form_intelect})
    