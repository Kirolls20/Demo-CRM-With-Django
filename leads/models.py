from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

COUNTRY_NAMES=(
   ('USA','USA'),
   ('Canada','Canada'),
   ('Australia','Australia'),
   ('Egypt','Egypt'),
   ('Germany','Germany'),
   ('England','England')

)
SOURCE_CHOICES= (
   ("Facebook","Facebook"),
   ("Twitter","Twitter"),
   ("Instagram","Instagram"),
   ("Youtube","Youtube"),
   ("Newspaper","Newspaper"),
   ("Other","other"),
)

class User(AbstractUser):
   first_name= models.CharField(max_length=50)
   last_name= models.CharField(max_length=50)
   age = models.IntegerField(default=0)
   
   phone_number= models.CharField(max_length=15)
   job_title= models.CharField(max_length=100)
   profile_pic = models.ImageField(null=True, blank=True, default="images/profile/profile_pic.jpg", upload_to="images/profile/")
   joined_time= models.DateTimeField(auto_now_add=True)
   


class Lead(models.Model):
   first_name= models.CharField(max_length=50)
   last_name= models.CharField(max_length=50)
   email= models.EmailField()
   age=models.IntegerField(default=0)
   country = models.CharField(choices=COUNTRY_NAMES,max_length=150,default='USA')
   source= models.CharField(choices=SOURCE_CHOICES,max_length=150)
   agent= models.ForeignKey("Agent",on_delete=models.CASCADE,related_name='agent')
   existed_from= models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
   user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.user.username
   


