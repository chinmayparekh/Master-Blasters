from django.shortcuts import render
from recruiter.models import Recruiter_Post,Skills_Reqd,Eligible_Colleges
# Create your views here.

def home(request):
    return render(request,"view_posts.html")
def view_posts(request):
    college_name = "IIITB"#change this . Take from logged in name
    cols = Eligible_Colleges.objects.filter(college_name=college_name)
    # print(cols)
    for i in cols:
        print(i.post_id.company)
        print(i.college_name)
    relevant_posts = [i.post_id for i in cols]

    return render(request,"view_posts.html",{"posts":relevant_posts})
