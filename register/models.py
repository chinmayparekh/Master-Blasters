from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Recruiter(models.Model):
    Company_name = models.CharField(max_length=100)
    Company_website = models.URLField()
    Company_linkedin = models.URLField()
    Company_email = models.EmailField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.Company_name


class Pcell(models.Model):
    College_name = models.CharField(max_length=100)
    College_website = models.URLField()
    College_linkedin = models.URLField()
    College_email = models.EmailField()
    College_location = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.College_name
