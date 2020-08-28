from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
from django_mysql.models import DynamicField,JSONField
# Create your models here.

class DoctorManager(BaseUserManager):

    def create_user(self,username,password=None):

        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password):
        
        user = self.create_user(
            password=password,
            username = username,

        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Doctor(AbstractBaseUser):
    username    =  models.CharField(max_length=50,unique=True)
    email       =  models.EmailField(max_length=254,unique=True)
    last_login  =  models.DateTimeField(auto_now=True)
    is_admin    =  models.BooleanField(default=False)
    is_active   =  models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff    =  models.BooleanField(default=False)

    name = models.CharField(max_length=254,null=True)
    contact_no = models.CharField(max_length=10)

    USERNAME_FIELD = 'username'

    #specifying manager
    objects = DoctorManager()


    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

class Visitors(models.Model):
    account = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    entries = JSONField(default=list)
