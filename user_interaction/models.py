from django.db import models

# Create your models here.
class user_detail(models.Model):
    full_name = models.CharField(max_length=264)
    user_name = models.CharField(max_length=264,unique=True,primary_key=True)
    management_name = models.CharField(max_length=264)
    contact_no = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=254)
    designation = models.CharField(max_length=264)
    department = models.CharField(max_length=264)
    #prof_pic pending still 
