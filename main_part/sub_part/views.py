from tkinter.constants import END
from django.shortcuts import render,redirect
from .models import adminlogin,adminregister,userlogin,userregister,aduserlist,ussleave,addesignation,adcategory,adnotice,adupdateinfo,adupdatepassword,usupdateinfo,usupdatepassword,indexform,adholiday,addindividual,adsummary
from django.conf import settings
from django.core.mail import send_mail
import easygui


# Create your views here.
def index(request):
    
    return render(request,'index.html')
def index1(request):
    if request.method=='POST':
        indexform_dis=indexform(name=request.POST['name'],
                                email=request.POST['email'],
                                message=request.POST['message'],
                                )
        indexform_dis.save()

        subject = 'Thank YoU FoR Getting In Touch.!!'
        message = 'We appreciate you Contacting Us.  One Of Our Colleagues will get back in Touch With YOu soon!!    Have a Great DaY!'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print("check:",recepient)
        send_mail (subject,
            message,email_from,[recepient],fail_silently = False)

        easygui.msgbox("your data has been stored successfully",title="presence")
        return render(request,'index.html')
    return render(request,'index.html')
def admin_dashboard(request):
    if request.method=="POST":
        adminlogin_dis=adminlogin(userid=request.POST['userid'],
                                  enterpassword=request.POST['enterpassword'],
                                  )
        adminlogin_dis.save()
        if adminregister.objects.filter(userid=request.POST['userid'],
                                     enterpassword=request.POST['enterpassword'],
                                     ).exists():
             val1=adminregister.objects.get(userid=request.POST['userid'],
                                            enterpassword=request.POST['enterpassword'],
                                            )
             easygui.msgbox("your data has been stored successfully",title="presence")
             return redirect(adminindex)
        else:
            context={'msg':'Oops! you entered wrong details'}
            return render(request,'admin_dashboard.html',context)
    return render(request,'admin_dashboard.html')
def adminreg(request):
    if request.method=="POST":
        adminregister_dis=adminregister(userid=request.POST['userid'],
                                        emailid=request.POST['emailid'],
                                        enterpassword=request.POST['enterpassword'],
                                        )
        adminregister_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
        return redirect(admin_dashboard)
    return render (request,'admin_dashboard.html')
def admincategory(request):
    if request.method=="POST":
        adcategory_dis=adcategory(name=request.POST['name'],
                                  year=request.POST['year'],
                                  )
        adcategory_dis.save()
        easygui.msgbox("your data has been stored sucessfully",title="presence")
        return redirect(admincategory1)
    return render(request,'admincategory.html')
def admincategory1(request):
    var2=adcategory.objects.all()
    return render(request,'admincategory.html',{'var2':var2})
def adcategory_edit(request,id):
    ex2=adcategory.objects.get(id=id)
    return render(request,'adcategory_edit.html',{'ex2':ex2})
def adcategory_update(request,id):
    ex2=adcategory(id=id ,name=request.POST['name'],
                               year=request.POST['year'],
                               )
    ex2.save()
    easygui.msgbox("your data has been updated successfully",title="presence")
    return redirect(admincategory1)
def adcategory_delete(request,id):
    ex2=adcategory.objects.get(id=id)
    ex2.delete()
    easygui.msgbox("your data has been deleted",title="presence")
    return redirect(admincategory1)
def adminDesignation(request):
    if request.method=="POST":
        addesignation_dis=addesignation(name=request.POST['name'],
                                        )
        addesignation_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence") 
        return redirect(adminDesignation1)
        
   
    return render(request,'adminDesignation.html')
def adminDesignation1(request):
     dish=addesignation.objects.all()
     return render(request,'adminDesignation.html',{'dish':dish})
    
def adminholiday(request):
    if request.method=='POST':
        adholiday_dis=adholiday(hdate=request.POST['hdate'])
        adholiday_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
    return redirect(adminholiday1)
def adminholiday1(request):
    var5=adholiday.objects.all()
    return render(request,'adminholiday.html',{'var5':var5})
def adholiday_edit(request,id):
    ex5=adholiday.objects.get(id=id)
    return render(request,'adholiday_edit.html',{'ex5':ex5})
def adholiday_update(request,id):
    ex5=adholiday(id=id, hdate=request.POST['hdate'])
    ex5.save()
    easygui.msgbox("Your data has been updated successfully",title="presence")
    return redirect(adminholiday1)
def adholiday_delete(request,id):
    ex5=adholiday.objects.get(id=id)
    ex5.delete()
    easygui.msgbox("your data has been deleted",title="presence")
    return redirect(adminholiday1)
def adminindex(request):
    var3=adnotice.objects.all()
    return render (request,'adminindex.html',{'var3':var3})
   
def adminindividual(request):
     if request.method=='POST':
        addindividual_dis=addindividual(date=request.POST['date'],
                                      intime=request.POST['intime'],
                                      outtime=request.POST['outtime'],
                                      worked=request.POST['worked'],
                                      status=request.POST['status'],)
        addindividual_dis.save()
        easygui.msgbox("your data has been updated successfully",title="presence")
        return redirect(adminindividual1)
     return render(request,'adminindividual.html')
    
def adminindividual1(request):
    var7=addindividual.objects.all()
    return render(request,'adminindividual.html',{'var7':var7})
def adinidivdual_edit(request,id):
    ex7=addindividual.objects.get(id=id)
    return render(request,'adindividual_edit.html',{'ex7':ex7})  
def adindividual_update(request,id):
    ex7=addindividual(id=id,date=request.POST['date'],
                            intime=request.POST['intime'],
                            outtime=request.POST['outtime'],
                            worked=request.POST['worked'],
                            status=request.POST['status'],) 
    ex7.save()
    easygui.msgbox("your data has been updated successfully",title="presence")
    return redirect(adminindividual1)
def adindividual_delete(request,id):
    ex7=addindividual.Objects.get(id=id)
    ex7.delete()
    easygui.msgbox("your data has been deleted")
    return redirect(adminindividual1)
def adminleave(request):
    var4=ussleave.objects.all()
    return render(request,'adminleave.html',{'var4':var4})
def adleave_edit(request,id):
    ex4=ussleave.objects.get(id=id)
    return render(request,'adleave_edit.html',{'ex4':ex4})
def adleave_update(request,id):
    ex4=ussleave(id=id, leavedate=request.POST['leavedate'],
                       leavecategory=request.POST['leavecategory'],
                       description=request.POST['description'],
                       status=request.POST['status'],)
    ex4.save()
    easygui.msgbox("your data has been updated successfully",title="presence")
    return redirect(adminleave)
def adleave_delete(request,id):
    ex4=ussleave.objects.get(id=id)
    ex4.delete()
    easygui.msgbox("your data has been deleted ",title="presence")
    return redirect(adminleave)
def usrleave(request):
    var4=ussleave.objects.all()
    return render(request,'userleave.html',{'var4':var4})
def adminnotice(request):
    if request.method=='POST':
        adnotice_dis=adnotice(subject=request.POST['subject'],
                              message=request.POST['message'],
                              )
        adnotice_dis.save()
        easygui.msgbox("your data hasbeen stored successfully",title="presence")
        return redirect(adminnotice1)
    return render(request,'adminnotice1.html')
def adminnotice1(request):
    var3=adnotice.objects.all()
    return render (request,'adminnotice.html',{'var3':var3})
def adnotice_edit(request,id):
    ex3=adnotice.objects.get(id=id)
    return render(request,'adnotice_edit.html',{'ex3':ex3})
def adnotice_update(request,id):
    ex3=adnotice(id=id,subject=request.POST['subject'],
                        message=request.POST['message'],
                        )
    ex3.save()
    easygui.msgbox("your data has been updated successfully",title="presence")
    return redirect(adminnotice1)
def adnotice_delete(request,id):
    ex3=adnotice.objects.get(id=id)
    ex3.delete()
    easygui.msgbox("your data has been deleted",title="presence")
    return redirect(adminnotice1)

def adminsummary(request):
    if request.method=='POST':
        adsummary_dis=adsummary(name=request.POST['name'],
                                worked=request.POST['worked'],)
        adsummary_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
        return redirect(adminsummary1)
    return render(request,'adminsummary.html')
def adminsummary1(request):
    var7=adsummary.objects.all()
    return render(request,'adminsummary.html',{'var7':var7})
def adsummary_edit(request,id):
    ex7=adsummary.objects.get(id=id)
    return render(request,'adsummary_edit.html',{'ex7':ex7})
def adsummary_update(request,id):
    ex7=adsummary(id=id,name=request.POST['name'],
                        worked=request.POST['worked'],)
    ex7.save()
    easygui.msgbox("your data has been updated successfully",title="presence")
    return redirect(adminsummary1)
def adsummary_delete(request,id):
    ex7=adsummary.objects.get(id=id)
    ex7.delete()
    easygui.msgbox("your data has been deleted",title="presence")
    return redirect(adminsummary1)
def adminupdateinfo(request):
    if request.method=='POST':
        adupdateinfo_dis=adupdateinfo(name=request.POST['name'],
                                      email=request.POST['email'],
                                      timezone=request.POST['timezone'],
                                      title=request.POST['title'],
                                      footer=request.POST['footer'],
                                      )
        adupdateinfo_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
        return redirect(adminupdateinfo)
    return render(request,'adminupdateinfo.html')
def adminupdatepassword(request):
    var8=adminregister.objects.all()
    return render(request,'adminupdatepassword.html',{'var8':var8})

def adupdatepassword_edit(request,id):
    ex8=adminregister.objects.get(id=id)
    return render(request,'adupdatepassword_edit.html',{'ex8':ex8})
def adupdatepassword_update(request,id):
    ex8=adminregister(id=id,userid=request.POST['userid'],
                            emailid=request.POST['emailid'],
                            enterpassword=request.POST['enterpassword'],)
    ex8.save()
    easygui.msgbox("Your data has been updated successfully",title="Presence")
    return redirect(adminupdatepassword)
def adupdatepassword_delete(request,id):
    ex8=adminregister.objects.get(id=id)
    ex8.delete()
    easygui.msgbox("your data has been deleted",title="presence")
    return redirect(adminupdatepassword)
def adminuserlist(request):
    if request.method=='POST':
        aduserlist_dis=aduserlist(name=request.POST['name'],
                                  email=request.POST['email'],
                                  password=request.POST['password'],
                                  retypepassword=request.POST['retypepassword'],
                                  )
        aduserlist_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
        return redirect(adminuserlist1)
    
    return render(request,'adminuserlist.html')
def adminuserlist1(request):
    adusrlist=aduserlist.objects.all()
    return render(request,'adminuserlist.html',{'adusrlist':adusrlist})
def aduserlist_edit(request,id):
    ex1=aduserlist.objects.get(id=id)
    return render(request,'aduserlist_edit.html',{'ex1':ex1})
def aduserlist_update(request,id):
    ex1=aduserlist(id=id, name=request.POST['name'],
                          email=request.POST['email'],
                          password=request.POST['password'],
                          retypepassword=request.POST['retypepassword'],)
    ex1.save()
    easygui.msgbox("your data has been updated successfully",title="presence")
    return redirect(adminuserlist1)
def aduserlist_delete(request,id):
    ex1=aduserlist.objects.get(id=id)
    ex1.delete()
    easygui.msgbox("your data has been deleted successfully",title="presence")
    return redirect(adminuserlist1)
def userholiday(request):
    var5=adholiday.objects.all()
    return render(request,'userholiday.html',{'var5':var5})
    
def userindex(request):
    var3=adnotice.objects.all()
    return render(request,'userindex.html',{'var3':var3})
def userindividual(request):
    var7=addindividual.objects.all()
    return render(request,'userindividual.html',{'var7':var7})
def userleave(request):
    if request.method=='POST':
        ussleave_dis=ussleave(
                            leavedate=request.POST['leavedate'],
                            leavecategory=request.POST['leavecategory'],
                            description=request.POST['description'],
                            status=request.POST['status'],
                            )
        ussleave_dis.save()
        easygui.msgbox("your data hasbeen stored successfully",title="presence")
        return redirect(usrleave)
    return render(request,'userleave.html')


def usernotice(request):
    var3=adnotice.objects.all()
    return render(request,'usernotice.html',{'var3':var3})
def userupdateinfo(request):
    if request.method=='POST':
        usupdateinfo_dis=usupdateinfo(name=request.POST['name'],
                                      email=request.POST['email'],
                                      )
        usupdateinfo_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
        return redirect(userupdateinfo)
    return render(request,'userupdateinfo.html')
def userupdatepassword(request):
   var9=userregister.objects.all()
   return render(request,'userupdatepassword.html',{'var9':var9})
def usupdatepassword_edit(request,id):
    ex9=userregister.objects.get(id=id)
    return render(request,'usupdatepassword_edit.html',{'ex9':ex9})
def usupdatepassword_update(request,id):
    ex9=userregister(id=id,userid=request.POST['userid'],
                            emailid=request.POST['emailid'],
                            enterpassword=request.POST['enterpassword'],)
    ex9.save()
    easygui.msgbox("Your data has been updated successfully",title="Presence")
    return redirect(userupdatepassword)
def usupdatepassword_delete(request,id):
    ex9=userregister.objects.get(id=id)
    ex9.delete()
    easygui.msgbox("your data has been deleted",title="presence")
    return redirect(userupdatepassword)
def user(request):
    if request.method=='POST':
        userlogin_dis=userlogin(userid=request.POST['userid'],
                                enterpassword=request.POST['enterpassword'],
                                )
        userlogin_dis.save()
        if userregister.objects.filter(userid=request.POST['userid'],
                                       enterpassword=request.POST['enterpassword'],
                                       ).exists():
            val2=userregister.objects.get(userid=request.POST['userid'],
                                          enterpassword=request.POST['enterpassword'],
                                          )
            easygui.msgbox("your data has been stored successfully",title="presence")
            return redirect(userindex)
        else:
            context2={'msg':'Oops! you entered wrong details'}
            return render(request,'user.html',context2)
    return render(request,'user.html')
def userreg(request):
    if request.method=='POST':
        userregister_dis=userregister(userid=request.POST['userid'],
                                      emailid=request.POST['emailid'],
                                      enterpassword=request.POST['enterpassword'],
                                      )
        userregister_dis.save()
        easygui.msgbox("your data has been stored successfully",title="presence")
        return redirect(user)
    return render(request,'user.html')

def addesignation_edit (request,id):
    ex=addesignation.objects.get(id=id)
    return render(request,'addesignation_edit.html',{'ex':ex})

def addesignation_update(request,id):
    ex=addesignation(id=id,name=request.POST['name'],)
    ex.save()
    easygui.msgbox("your data has been updated sucessfully",title="presence")
    return redirect(adminDesignation1)

def addesignation_delete(request,id):
    ex=addesignation.objects.get(id=id)
    ex.delete()
    easygui.msgbox("your data has been deleted")
    return redirect(adminDesignation1)
