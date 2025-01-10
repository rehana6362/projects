from django.contrib import admin
from .models import Candidate, PersonalInformation, AdditionalInformation, WorkExperience

class PersonalInformationInline(admin.TabularInline):
    model = PersonalInformation
    extra = 1  

class AdditionalInformationInline(admin.TabularInline):
    model = AdditionalInformation
    extra = 1  

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1 

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_name','education')
    inlines=[PersonalInformationInline,AdditionalInformationInline,WorkExperienceInline]