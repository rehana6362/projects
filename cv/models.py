from django.db import models

# Create your models here.
class Candidate(models.Model):
    company_logo = models.ImageField(upload_to='candidate_images/')
    candidate_name = models.CharField(max_length=100)
    candidate_image = models.ImageField(upload_to='candidate_images/')
    careersummary = models.CharField(max_length=400)
    education = models.TextField()
    self_project = models.TextField()

    def __str__(self):
        return self.candidate_name

class PersonalInformation(models.Model):
    Candidate =  models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name='candidates',)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.gender}, {self.nationality}, {self.status}"


class AdditionalInformation(models.Model):
    Candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name='additional_skills')
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill


class WorkExperience(models.Model):
    Candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name='work_experiences')
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    period = models.CharField(max_length=100)  # Example: "Jan 2020 - Dec 2023"
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"


