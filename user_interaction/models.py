from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
# Create your models here.

class StudentAccountManager(BaseUserManager):
    #to overwrite   create_user  and  create_superuser 

    def create_user(self,username,password=None):
        # if not email:
        #     raise ValueError("Users must have an email address")
        
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






class StudentAccount(AbstractBaseUser):
    username    =  models.CharField(max_length=50,unique=True)
    email       =  models.CharField(max_length=264,unique=True)
    joined_date =  models.DateTimeField(auto_now_add=True)
    last_login  =  models.DateTimeField(auto_now=True)
    is_admin    =  models.BooleanField(default=False)
    is_active   =  models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff    =  models.BooleanField(default=False)


    management_name = models.CharField(max_length=264)
    full_name = models.CharField(max_length=264,null=True)
    contact_no = models.CharField(max_length=10)
    department = models.CharField(max_length=264)
    residential_status = models.CharField(max_length=264)
    

    USERNAME_FIELD = 'username'

    #specifying manager
    objects = StudentAccountManager()


    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True