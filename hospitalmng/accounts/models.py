from django.db import models

# Create your models here.
class Staff(models.Model):
    first=models.CharField(max_length=100,verbose_name='Enter First Name')
    last=models.CharField(max_length=100,verbose_name='Enter Last Name')
    username=models.CharField(max_length=100,verbose_name='Enter UserName')
    experience=models.IntegerField(verbose_name='Enter Experience')
    password=models.CharField(max_length=100,verbose_name='Enter password')
    email=models.EmailField(verbose_name='Enter Email')
    pic=models.ImageField(upload_to="profile_pic",null=True)
    
    def __str__(self):
        return self.first