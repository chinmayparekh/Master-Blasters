from django.shortcuts import render

# Create your views here.

def make_post(request):

    if ("company" in request.GET):
        print(request.GET["company"])
        print(request.GET["position"])
        print(request.GET["skills"])

    return render(request,"recruiter_post.html")

