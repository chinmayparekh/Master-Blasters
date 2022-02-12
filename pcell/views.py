from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"view_posts.html")
def view_posts(request):
    return render(request,"view_posts.html")
