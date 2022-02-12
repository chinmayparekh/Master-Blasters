from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RecRegisterForm(UserCreationForm):
    Company_name = forms.CharField(max_length=100)
    Company_website = forms.URLField()
    Company_linkedin = forms.URLField()
    Company_email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "Company_name", "Company_website",
                  "Company_linkedin", "Company_email", "password1", "password2")

    def save(self, commit=True):
        user = super(RecRegisterForm, self).save(commit=False)
        user.Company_name = self.cleaned_data["Company_name"]
        user.Company_email = self.cleaned_data["Company_email"]
        user.Company_website = self.cleaned_data["Company_website"]
        user.Company_linkedin = self.cleaned_data["Company_linkedin"]
        if commit:
            user.save()
        return user


class CellRegisterForm(UserCreationForm):
    College_name = forms.CharField(max_length=100)
    College_website = forms.URLField()
    College_linkedin = forms.URLField()
    College_email = forms.EmailField()
    College_location = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "College_name", "College_website", "College_linkedin",
                  "College_email", "College_location", "password1", "password2")

    def save(self, commit=True):
        user = super(CellRegisterForm, self).save(commit=False)
        user.College_name = self.cleaned_data["College_name"]
        user.College_email = self.cleaned_data["College_email"]
        user.College_website = self.cleaned_data["College_website"]
        user.College_linkedin = self.cleaned_data["College_linkedin"]
        user.College_location = self.cleaned_data["College_location"]
        if commit:
            user.save()
        return user
