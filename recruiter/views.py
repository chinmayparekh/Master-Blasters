from django.shortcuts import render, redirect
from recruiter.models import Recruiter_Post, Skills_Reqd, Eligible_Colleges
from register.models import Pcell, Recruiter


# Create your views here.

def home(request):
    return render(request, "home.html")


def make_post(request):
    if (request.method == "POST"):

        rp = Recruiter_Post(
            company=request.POST["company"],
            position=request.POST["position"],

            workmode=request.POST["workmode"],
            location=request.POST["location"],

            # skills = request.POST.getlist("skills"),
            description=request.POST["description"]

        )
        print("before save")
        print(rp)
        rp.save()

        # print([i.id for i in Recruiter_Post.objects.all()])

        # print(type(request.POST.getlist("skills")))
        for i in range(len(request.POST.getlist("skills"))):
            # pass

            sk = Skills_Reqd(
                post_id=rp,
                skill=request.POST.getlist("skills")[i]

            )

            sk.save()

        return redirect("filter_posts")

        # return render(request,"filter_posts.html")

    # testing
    # print(Recruiter_Post.objects.all())
    # for i in Recruiter_Post.objects.all():
    #     print(i.company)
    #     print(Skills_Reqd.objects.filter(post_id=rp))
    #     for j in Skills_Reqd.objects.filter(post_id=rp):
    #         print(j.skill)
    #     print(i.location)
    # for j in i.skills:
    #     print(j)

    username = request.user.username
    company_name = Recruiter.objects.filter(username=username)[0].Company_name

    return render(request, "recruiter_post.html", {"company_name": company_name})


def filter_posts(request):
    if (request.method == 'GET' and "location1" in request.GET):
        # print(request.GET.get("location1"))
        loc_list = [request.GET.get("location" + str(i)) for i in range(1, 4) if request.GET.get("location" + str(i))]
        all_flag = False
        colleges = []

        if (not loc_list):
            all_flag = True

        if (not all_flag):
            for j in loc_list:
                if (j):
                    print(j)
                    colleges.extend([i.College_name for i in Pcell.objects.filter(College_location=j)])
        else:
            colleges = [i.College_name for i in Pcell.objects.all()]
        print(loc_list, colleges)
        for i in Pcell.objects.all():
            print(i.College_location)

        return render(request, "filter_posts.html", {"flag": 1, "colleges": colleges})

    else:
        if ('colleges' in request.POST):
            username = request.user.username
            details = Recruiter.objects.get(username=username)
            filtered_colleges = request.POST.getlist("colleges")
            print(filtered_colleges)
            print("Latest comp", Recruiter_Post.objects.last().company)
            for i in filtered_colleges:
                ec = Eligible_Colleges(
                    post_id=Recruiter_Post.objects.last(),
                    college_name=i
                )
                ec.save()
            return render(request, 'recruiterProfile.html', {"details": details})


        return render(request, "filter_posts.html", {"flag": 0})
