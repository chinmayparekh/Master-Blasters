from django.shortcuts import render
from recruiter.models import Recruiter_Post,Skills_Reqd,Eligible_Colleges
from register.models import Pcell


# Create your views here.

def home(request):
    return render(request,"home.html")

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
            
            # skills = request.POST.getlist("skills"),
            description = request.POST["description"]
            
    
    
        )
        rp.save()
        # print(type(request.POST.getlist("skills")))
        for i in range(len(request.POST.getlist("skills"))):
            # pass
            
            sk =Skills_Reqd(
                post_id=rp,
                skill = request.POST.getlist("skills")[i]

            )

            sk.save()

        return render(request,"filter_posts.html")

    #testing
    # print(Recruiter_Post.objects.all())
        # for i in Recruiter_Post.objects.all():
        #     print(i.company)
        #     print(Skills_Reqd.objects.filter(post_id=rp))
        #     for j in Skills_Reqd.objects.filter(post_id=rp):
        #         print(j.skill)
        #     print(i.location)
        # for j in i.skills:
        #     print(j)




    return render(request,"recruiter_post.html")


def filter_posts(request):
    
    if (request.method=='GET' and "location1" in request.GET):
        # print(request.GET.get("location1"))
        loc_list = [request.GET.get("location"+str(i)) for i in range(1,4) if request.GET.get("location"+str(i))]
        all_flag=False
        colleges=[]


        #the filtering part is needed here for the collges based on location
        if (not loc_list):
            all_flag=True
        
        if (not all_flag):
            for j in loc_list:
                if (j):
                    print(j)
                    colleges.extend([i.College_name for i in Pcell.objects.filter(College_location = j)])
        else:
            colleges = [i.College_name for i in Pcell.objects.all()]
        print(loc_list,colleges)
        for i in Pcell.objects.all():
            print(i.College_location)

        return render(request,"filter_posts.html",{"flag":1,"colleges":colleges})

    else:
        filtered_colleges = request.POST.getlist("colleges")
        print(filtered_colleges)
        print("Latest comp",Recruiter_Post.objects.last().company)
        for i in filtered_colleges:
            ec = Eligible_Colleges(
                post_id=Recruiter_Post.objects.last(),
                college_name = i
            )
            ec.save()
           
    return render(request,"filter_posts.html",{"flag":0})
