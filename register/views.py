from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CellRegisterForm, RecRegisterForm
from .models import Recruiter, Pcell
# Create your views here.

def home(request):
    return render(request, 'register/home.html')
    
    
def register_cell(request):
    if request.method == 'POST':
        form = CellRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            College_name = form.cleaned_data["College_name"]
            College_email = form.cleaned_data["College_email"]
            College_linkedin = form.cleaned_data["College_linkedin"]
            College_website = form.cleaned_data["College_website"]
            College_location = form.cleaned_data["College_location"]

            cell = Pcell(username=username,College_name=College_name, College_email=College_email, College_linkedin=College_linkedin,
                         College_website=College_website, College_location=College_location)
            cell.save()
            messages.success(request, f'Account created for {username}!')

            return redirect('login')
    else:
        form = CellRegisterForm()
    return render(request, 'register/register.html', {'form': form})


def register_rec(request):
    if request.method == 'POST':
        form = RecRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            Company_name = form.cleaned_data["Company_name"]
            Company_email = form.cleaned_data["Company_email"]
            Company_linkedin = form.cleaned_data["Company_linkedin"]
            Company_website = form.cleaned_data["Company_website"]

            rec = Recruiter(username=username,Company_name=Company_name, Company_email=Company_email,
                            Company_linkedin=Company_linkedin, Company_website=Company_website)
            rec.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('register-home')
    else:
        form = RecRegisterForm()
    return render(request, 'register/register.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'register/register.html')
    
    username = request.user.username
    
    if Recruiter.objects.filter(username=username):
        # Go to recruiter home page
        return render(request, '../../recruiter/templates/recruiterProfile.html')
    else:
        # go to pcell home page
        return render(request, 'register/pcellProfile.html')
    print(username)    
