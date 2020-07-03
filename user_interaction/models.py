from django.db import models

# Create your models here.
class user_detail(models.Model):
    full_name = models.CharField(max_length=264)
    roll_no = models.CharField(max_length=264,unique=True,primary_key=True)
    management_name = models.CharField(max_length=264)
    contact_no = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=264)
    residential_status = models.CharField(max_length=264)
    #prof_pic pending still 

class staff_user_detail(models.Model):
    emp_id = models.CharField(max_length=264,unique=True,primary_key=True)
    full_name = models.CharField(max_length=264)
    departmment = models.CharField(max_length=264)
    designation = models.CharField(max_length=264)
    contact_no = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=254)
    residential_status = models.CharField(max_length=264)