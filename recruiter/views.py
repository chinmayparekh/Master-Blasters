from django.shortcuts import render
from recruiter.models import Recruiter_Post

# Create your views here.

def make_post(request):

    # if ("company" in request.GET):
    #     print(request.GET["company"])
    #     print(request.GET["position"])
    #     print(request.GET["skills"])

    if (request.method=="POST"):
        # print(request.POST)
        # print((request.POST.getlist("skills")))
        # print(request.POST)
        rp = Recruiter_Post (
            company = request.POST["company"],
            position = request.POST["position"],

            workmode =  request.POST["workmode"],
            location =  request.POST["location"],
            
            skills = request.POST.getlist("skills"),
            description = request.POST["description"]
            
    
    
        )
        rp.save()

    #testing
    print(Recruiter_Post.objects.all())
    for i in Recruiter_Post.objects.all():
        print(i.company)
        print(i.skills)
        print(i.location)
        # for j in i.skills:
        #     print(j)




    return render(request,"recruiter_post.html")

