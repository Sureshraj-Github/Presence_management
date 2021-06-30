from django.db import models


# Create your models here.

class adminlogin(models.Model):
    userid=models.CharField(max_length=100)
    enterpassword=models.CharField(max_length=100)

    def __str__(self):
        return self.userid

class adholiday(models.Model):
    hdate=models.CharField(max_length=100)

    def __str__(self):
        return self.hdate

class adminregister(models.Model):
     userid=models.CharField(max_length=100)
     emailid=models.EmailField()
     enterpassword=models.CharField(max_length=100)

     def __str__(self):
        return self.userid

class userlogin(models.Model):
     userid=models.CharField(max_length=100)
     enterpassword=models.CharField(max_length=100)

     def __str__(self):
        return self.userid

class userregister(models.Model):
    userid=models.CharField(max_length=100)
    emailid=models.EmailField()
    enterpassword=models.CharField(max_length=100)

    def __str__(self):
        return self.userid

class aduserlist(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    retypepassword=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class addesignation(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class adcategory(models.Model):
    name=models.CharField(max_length=100)
    year=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class adnotice(models.Model):
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.subject

class adupdateinfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    timezone=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    footer=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class adupdatepassword(models.Model):
    oldpassword=models.CharField(max_length=100)
    newpassword=models.CharField(max_length=100)
    retypepassword=models.CharField(max_length=100)

    def __str__(self):
        return self.oldpassword

class ussleave(models.Model):
    
    leavedate=models.CharField(max_length=100)
    leavecategory=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.leavedate

class usupdateinfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class usupdatepassword(models.Model):
    oldpassword=models.CharField(max_length=100)
    newpassword=models.CharField(max_length=100)
    retypepassword=models.CharField(max_length=100)

    def __str__(self):
        return self.oldpassword

class indexform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class addindividual(models.Model):
    date=models.CharField(max_length=100)
    intime=models.CharField(max_length=100)
    outtime=models.CharField(max_length=100)
    worked=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.date

class adsummary(models.Model):
    name=models.CharField(max_length=100)
    worked=models.CharField(max_length=100)

    def __str__(self):
        return self.name