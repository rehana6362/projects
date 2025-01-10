from django.shortcuts import render
from .models import Candidate, PersonalInformation, AdditionalInformation, WorkExperience

def home(request):
    return render(request, 'cv/detail.html')

def candidate_list(request, candidate_id):
    # Retrieve the candidate based on the provided ID
    candidate = Candidate.objects.get(id=candidate_id)

    # Retrieve related data from PersonalInformation, AdditionalInformation, and WorkExperience
    personal_info = PersonalInformation.objects.filter(Candidate=candidate)
    additional_info = AdditionalInformation.objects.filter(Candidate=candidate)
    work_experience = WorkExperience.objects.filter(Candidate=candidate)

    # Pass all the data to the template
    context = {
        'candidate': candidate,
        'personal_info': personal_info,
        'additional_info': additional_info,
        'work_experience': work_experience,
    }

    return render(request, 'cv/candidate_list.html', context)
