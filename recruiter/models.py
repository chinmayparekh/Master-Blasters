from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Recruiter_Post(models.Model):

    company = models.CharField(max_length = 200)
    position = models.CharField(max_length = 150)

    workmode =  models.CharField(max_length = 40)
    location =  models.CharField(max_length = 400)
    
    description = models.CharField(max_length = 500)
    
    eligible_colleges=ArrayField(models.CharField(max_length=200), blank=True)
    



    