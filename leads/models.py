from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


SOURCE_CHOICES= (
   ("Facebook","Facebook"),
   ("Twitter","Twitter"),
   ("Instagram","Instagram"),
   ("Youtube","Youtube"),
   ("Newspaper","Newspaper"),
   ("Other","other"),
)

class User(AbstractUser):
   pass

class Lead(models.Model):
   first_name= models.CharField(max_length=50)
   last_name= models.CharField(max_length=50)
   email= models.EmailField()
   age=models.IntegerField(default=0)
   source= models.CharField(choices=SOURCE_CHOICES,max_length=150)
   agent= models.ForeignKey("Agent",on_delete=models.CASCADE,related_name='agent')
   existed_from= models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
   user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.user.username
   


