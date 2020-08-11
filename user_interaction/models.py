from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
# from django.contrib.postgres.fields import ArrayField,HStoreField
from django_mysql.models import DynamicField,JSONField
from io import BytesIO
from django.core.files import File
from PIL import Image , ImageDraw
from user_interaction.custom_functions import generate_qr
# Create your models here.

def qrcode_directory_path(instance,filename):
    return 'qrcode_{0}/{1}'.format(instance.username,filename)





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
    email       =  models.EmailField(max_length=254,unique=True)
    joined_date =  models.DateTimeField(auto_now_add=True)
    last_login  =  models.DateTimeField(auto_now=True)
    is_admin    =  models.BooleanField(default=False)
    is_active   =  models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff    =  models.BooleanField(default=False)
    

    management_name = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254,null=True)
    contact_no = models.CharField(max_length=10)
    department = models.CharField(max_length=254)
    residential_status = models.CharField(max_length=254)
    batch_year = models.CharField(max_length=4,default='Null')
    entry_qrcode = models.ImageField(upload_to = qrcode_directory_path,null=True)  
    

    USERNAME_FIELD = 'username'

    #specifying manager
    objects = StudentAccountManager()


    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    def save(self, *args, **kwargs):
        qrstring = 'PSG' + 'CT' + 'AMCSPW' + 'STU' + 'RG' + self.batch_year[len(self.batch_year)-2]  + self.batch_year[len(self.batch_year)-1] + self.username[len(self.username)-2] + self.username[len(self.username)-1]
        qr_image = generate_qr(qrstring) 
        canvas = Image.new('RGB' , (250,250), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        fname = f'qr_code-{self.username}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.entry_qrcode.save(fname , File(buffer) , save=False)
        canvas.close()
        super().save(*args,**kwargs)

class Visitor(models.Model):
    timestamp = models.CharField(max_length = 40,unique = True)
    image = models.ImageField(upload_to ='images',blank=True,null=True)
    temperature = models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return self.timestamp

# class StudentEntryDetail(models.Model):
#     account = models.ForeignKey(StudentAccount,on_delete=models.CASCADE)
#     entries = ArrayField(
#                 HStoreField()            
#                 )

class StudentEntryDetail(models.Model):
    account = models.ForeignKey(StudentAccount,on_delete=models.CASCADE)
    entries = JSONField(default=list)
