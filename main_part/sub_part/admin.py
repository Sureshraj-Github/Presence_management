from django.contrib import admin
from .models import adminlogin,adminregister,userlogin,userregister,aduserlist,addesignation,adcategory,adnotice,adupdateinfo,adupdatepassword,ussleave,usupdateinfo,usupdatepassword,indexform,adholiday,addindividual,adsummary

# Register your models here.
admin.site.register(adminlogin)
admin.site.register(adminregister)
admin.site.register(userlogin)
admin.site.register(userregister)
admin.site.register(aduserlist)
admin.site.register(addesignation)
admin.site.register(adcategory)
admin.site.register(adnotice)
admin.site.register(adupdateinfo)
admin.site.register(adupdatepassword)
admin.site.register(ussleave)
admin.site.register(usupdateinfo)
admin.site.register(usupdatepassword)
admin.site.register(indexform)
admin.site.register(adholiday)
admin.site.register(addindividual)
admin.site.register(adsummary)