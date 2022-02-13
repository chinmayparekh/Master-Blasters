from django.contrib import admin

# Register your models here.
from .models import Recruiter_Post, Skills_Reqd, Eligible_Colleges

admin.site.register(Recruiter_Post)
admin.site.register(Skills_Reqd)
admin.site.register(Eligible_Colleges)
