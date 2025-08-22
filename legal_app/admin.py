from django.contrib import admin
from .models import Contact,FeedBack,User,LegalAdvisor,Service,ClientDocument

class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone"]
class Feedback_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","remarks"]


# Register your models here.
admin.site.register(Contact,Contact_Admin)
admin.site.register(FeedBack,Feedback_Admin)
admin.site.register(User)
admin.site.register(LegalAdvisor)
admin.site.register(Service)
admin.site.register(ClientDocument)

admin.site.site_header="Law Firm Admin Dashboard"
admin.site.site_title="Find Your Best Way Of Justice"
admin.site.index_title="Legal Firm"
