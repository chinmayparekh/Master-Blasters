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
        print(i.post_id.id)
        print(i.college_name)
    
    class special_model():
        def __init__(self,post,skills):
            self.post=post
            self.skills = skills

    relevant_posts = [i.post_id for i in cols]
    skills = [Skills_Reqd.objects.filter(post_id=i) for i in relevant_posts]
    to_html= [special_model(relevant_posts[i],skills[i]) for i in range(len(relevant_posts))]

    return render(request,"view_posts.html",{"posts":to_html})
