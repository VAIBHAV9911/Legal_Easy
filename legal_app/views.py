from django.shortcuts import render,redirect
from .models import Contact,User,Service,FeedBack,LegalAdvisor
from django.contrib import messages
# Create your views here.
def view_services(request):
    service_list=Service.objects.all() # select * from service
    context={
        "service_key":service_list
    }
    return render(request,'legal_app/html/view_services.html',context)

def our_advisor(request):
    advisor_list=LegalAdvisor.objects.all() # select * from service
    advisor_list={
        "advisory_key":advisor_list
    }
    return render(request,'legal_app/html/our_advisor.html',advisor_list)


def home(request):
    feedback=FeedBack.objects.all()
    data=[]
    for f in feedback:
        data.append(
            {
                "rating":f.rating,
                "remark":f.remarks,
                "name":f.name,
                "profile_pic":User.objects.filter(email=f.email)[0].profile_pic
            }
        )
    feedback_dict={
        "feedback_key":data
    }
    return render(request,'legal_app/html/index.html',feedback_dict)

def about_us(request):
    return render(request,'legal_app/html/about_us.html')

def contact_us(request):
    if request.method=="GET":
        return render(request,'legal_app/html/contact_us.html')
    if request.method=="POST":
        user_email=request.POST["email"]
        user_name=request.POST["name"]
        user_phone=request.POST["phone"]
        user_question=request.POST["question"]
        user_contact=Contact(name=user_name,email=user_email,
                            phone=user_phone,query=user_question)
        user_contact.save()
        messages.success(request,"Thank you for Contacting Us 🙏")
        return redirect("contact")