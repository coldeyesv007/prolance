import datetime

from django.db import models
from django.contrib.auth.models import User
from  datetime import datetime
from PIL import Image
from autoslug import AutoSlugField
# Create your models here.

class formregistration(models.Model):
   fname=models.CharField(max_length=30)
   lname=models.CharField(max_length=30)
   email = models.EmailField()
   mobile = models.IntegerField()
   gender = models.CharField(max_length=10)
   image = models.ImageField()
   job = models.CharField(max_length=20)
   jobtype =models.CharField(max_length=20)
   field = models.IntegerField()
   wage = models.IntegerField()
   location = models.CharField(max_length=30)
   uname = models.CharField( max_length=60)
   about = models.CharField(max_length=100000000000000000)
   created_date =models.DateField(auto_now_add=True)

class userimage(models.Model):
   user= models.OneToOneField(User,on_delete=models.CASCADE)
   image =models.ImageField(upload_to='default', default='default/avatar.jpeg')

   def __str__(self):
      return self.user.username



class reviews(models.Model):
   userget = models.CharField(max_length=20)
   ruser= models.CharField(User,max_length=20)
   subject = models.CharField(max_length=20)
   review = models.TextField(max_length=100,blank=True)
   rating = models.FloatField()
   rfname = models.CharField(max_length=20)
   rlname = models.CharField(max_length=20)
   rimg = models.ImageField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)




class Messages(models.Model):
   msgget = models.CharField(max_length=30)
   value = models.CharField(max_length=10000)
   time = models.TimeField(auto_now_add=True, blank=True)
   sender = models.CharField(max_length=20)
   receiver = models.CharField(max_length=10000000000)
   mimg = models.ImageField()
   mfname = models.CharField(max_length=30)
   mlname = models.CharField(max_length=30)
   msgpost = models.CharField(max_length=30)
