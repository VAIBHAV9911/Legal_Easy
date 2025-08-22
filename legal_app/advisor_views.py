from django.shortcuts import render,redirect
from . models import LegalAdvisor,ClientDocument
from django.contrib import messages

def advisor_login(request):
    if request.method=="GET":
        return render(request,'legal_app/advisor/advisor_login.html')
    if request.method=="POST":
        user_email=request.POST["email"]
        user_password=request.POST["password"]
        user_list=LegalAdvisor.objects.filter(email=user_email,password=user_password)
        if len(user_list)>0:
            request.session["web_key"]=user_email #binding user to email in a session to track 
            return redirect("advisor_home")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("advisor_login")

def advisor_home(request):
        if request.method=="GET":
            user_email=request.session["web_key"]
            adv_obj=LegalAdvisor.objects.get(email=user_email) # it will return a single object 
        # sending data from veiw to html(template) page
        # create a dictionary and bind data with a key
        #send that dict with render function 
            adv_dict={"adv_key":adv_obj}
        return render(render,"legal_app/advisor/advisor_home.html",adv_dict)

def download_document(request):
    user_email=request.session["web_key"]
    document_list=  ClientDocument.objects.filter(advisor_email=user_email)
    doc_dict={
        "doc_key":document_list
        }
    return render(render,"legal_app/advisor/download_document.html",doc_dict)

def advisor_logout(request):
    request.session.flush()
    messages.success(request,"succesfully logged-out !!!!")
    return redirect ("advisor_login")
