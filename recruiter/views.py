from django.shortcuts import render
from recruiter.models import Recruiter_Post


# Create your views here.

def home(request):
    return render(request,"filter_posts.html")

def make_post(request):

    # if ("company" in request.GET):
    #     print(request.GET["company"])
    #     print(request.GET["position"])
    #     print(request.GET["skills"])

    if (request.method=="POST"):
       
        rp = Recruiter_Post (
            company = request.POST["company"],
            position = request.POST["position"],

            workmode =  request.POST["workmode"],
            location =  request.POST["location"],
            
            skills = request.POST.getlist("skills"),
            description = request.POST["description"]
            
    
    
        )
        rp.save()
        
        redirect

    #testing
    print(Recruiter_Post.objects.all())
    for i in Recruiter_Post.objects.all():
        print(i.company)
        print(i.skills)
        print(i.location)
        # for j in i.skills:
        #     print(j)




    return render(request,"recruiter_post.html")


def filter_posts(request):
    
    if (request.method=='GET' and "location1" in request.GET):
        # print(request.GET.get("location1"))
        loc_list = [request.GET.get("location"+str(i)) for i in range(1,4) if request.GET.get("location"+str(i))]
        all_flag=False
        colleges=["IIITB","NITK","RV","Thapar","IIT Delhi"]

        #the filtering part is needed here for the collges based on location
        if (not loc_list):
            all_flag=True

        print(loc_list,colleges)

        return render(request,"filter_posts.html",{"flag":1,"colleges":colleges})

    else:
        filtered_colleges = request.POST.getlist("colleges")
        print(filtered_colleges)
        
    return render(request,"filter_posts.html",{"flag":0})
