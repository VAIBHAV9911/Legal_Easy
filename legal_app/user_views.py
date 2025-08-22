from django.shortcuts import render,redirect
from .models import User,FeedBack,LegalAdvisor,ClientDocument
from django.contrib import messages

def user_edit_profile(request):
    if request.method=="GET":
        user_email=request.session["web_key"]
        user_obj=User.objects.get(email=user_email)
        user_dict={"user_key":user_obj}
        return render(request,"legal_app/user/user_edit_profile.html",user_dict)
    if request.method=="POST":
        user_name=request.POST["name"]
        user_phone=request.POST["phone"]
        user_pic=request.FILES.get("pic")
        user_email=request.session["web_key"]
        user_obj=User.objects.get(email=user_email)
        if user_pic is not None:
            user_obj.profile_pic=user_pic
        user_obj.name=user_name
        user_obj.phone=user_phone
        user_obj.save()
        messages.success(request,"profile updated successfully 👍")
        return redirect("user_home")

def user_logout(request):
    request.session.flush()
    messages.success(request,"succesfully logged-out !!!!")
    return redirect ("user_login")

def user_home(request):
    # fetching values from session to identify the user 
    if request.method=="GET":
        user_email=request.session["web_key"]
        user_obj=User.objects.get(email=user_email) # it will return a single object 
        # sending data from veiw to html(template) page
        # create a dictionary and bind data with a key
        #send that dict with render function 
        user_dict={"user_key":user_obj}
        return render(render,"legal_app/user/user_home.html",user_dict)

def user_login(request):
    if request.method=="GET":
        return render(request,'legal_app/user/user_login.html')
    if request.method=="POST":
        user_email=request.POST["email"]
        user_password=request.POST["password"]
        user_list=User.objects.filter(email=user_email,password=user_password)
        if len(user_list)>0:
            request.session["web_key"]=user_email #binding user to email in a session to track 
            return redirect("user_home")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("user_login")

def feedback(request):
    if request.method=="GET":
        return render(request,'legal_app/user/user_feedback.html')
    if request.method=="POST":
        user_name=request.POST["name"]
        user_email=request.session["web_key"]
        user_rating=request.POST["rating"]
        user_remarks=request.POST["remark"]
        user_feedback=FeedBack(name=user_name,email=user_email,rating=user_rating,
                    remarks=user_remarks)
        user_feedback.save()
        messages.success(request,"Thank you for your time 🙏")
        return redirect("feedback")

def registration(request):
    if request.method=="GET":
        return render(request,'legal_app/user/user_registration.html')
    if request.method=="POST":
        user_email=request.POST["email"] #control name input field
        user_password=request.POST["password"]
        user_name=request.POST["name"]
        user_phone=request.POST["phone"]
        user_pic=request.FILES["profile_pic"]
        ##ORM object relational mapping framework
        ## create object of user model
        ## set values ---> order should same as entered in the models file
        ## save object--> it automatically stores values in table
        user_obj=User(name=user_name,email=user_email,password=user_password,
                    phone=user_phone,profile_pic=user_pic)
        user_obj.save()
        return redirect("user_login")
    
def advisor_our(request):
    advisor_list = LegalAdvisor.objects.all()
    advisor_list={
        "advisory_key":advisor_list
    }
    return render(request,'legal_app/user/advisor_our.html',advisor_list)

def upload_document(request):
    if request.method=="GET":
        return render(request,'legal_app/user/upload_document.html')
    if request.method=="POST":
        user_email=request.session["web_key"]
        advisor_email = request.POST["advisor_email"]
        document_name=request.POST["document_name"]
        document_description=request.POST["document_description"]
        document_pic=request.FILES["document_pic"]
        user_obj = User.objects.get(email = user_email)
        Document=ClientDocument(user=user_obj,advisor_email=advisor_email,document_name=document_name,
                    document_description=document_description,document_pic=document_pic)
        Document.save()
        messages.success(request,"Thank you for your time 🙏")
        return redirect("upload_document")