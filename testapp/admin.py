from django.contrib import admin
from testapp.models import Sell1,Upload_Prescription,Buy1

class Sell1Admin(admin.ModelAdmin):
    list_display = ['Medicine','Name','Pincode','Location','Phoneno','Total_Amount','Batch_No','Email','quantity']

class Buy1Admin(admin.ModelAdmin):
    list_display = ['Medicine','Company_Name','Number_of_Tablet','Location','Phoneno','quantity','Pincode','Email','price']

class uploadAdmin(admin.ModelAdmin):
    list_display = ['prescrition']

admin.site.register(Buy1,Buy1Admin)
admin.site.register(Sell1,Sell1Admin)
admin.site.register(Upload_Prescription,uploadAdmin)
