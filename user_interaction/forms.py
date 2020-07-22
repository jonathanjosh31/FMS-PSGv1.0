from django import forms
import re
from .models import StudentAccount

class raw_user_form(forms.Form):
    full_name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class' : 'form-control-lg form-control reginput','placeholder' : 'Full Name','id':'reginput'}))
    roll_no = forms.CharField(label='Roll No',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Roll No'}))
    management_name = forms.CharField(label='Management Name',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Management Name'}))
    contact_no = forms.CharField(label='Contact No',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Contact No'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Email'}))
    residential_status = forms.CharField(label='Residential Status',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Residential Status'}))
    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Department'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Password'}))
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Confirm Password'}))

    def clean_full_name(self):
        data = self.cleaned_data.get('full_name')
        f=1
        for x in data:
            if not(x.isalpha() or x ==' '):
                f = 0
                break
        if (f==0):
            raise forms.ValidationError("Name doesn't shouldn't any numbers/Special characters!")
        if not(data[0] >='A' and data[0] <='Z'):
            raise forms.ValidationError("Your Name should begin with a capital letter")
        return data
    
    def clean_contact_no(self):
        data = self.cleaned_data.get('contact_no')

        if data.isdigit() == False:
             raise forms.ValidationError("Your Contact should only contain only digits/numbers!")
        if len(data) != 10 :
             raise forms.ValidationError("Your Contact should contain 10 digits!")
        return data
        
    
    def clean_password(self):
         data = self.cleaned_data.get('password')
         data1 = self.cleaned_data.get('confirm_password')
         fu=0
         fl=0
         fd=0
         if len(data) < 8 :
             raise forms.ValidationError("Length of password shoud be more than 7 characters!")
        
         for i in range(0,len(data)):
             if data[i].isupper():
                 fu=1
                 break
         if fu==0:
             raise forms.ValidationError("Password should contain atleast one uppercase letter!")
        
         for i in range(0,len(data)):
             if data[i].islower():
                 fl=1
                 break
         if fl==0:
             raise forms.ValidationError("Password should contain atleast one lowercase letter!")

         for i in range(0,len(data)):
             if data[i].isdigit():
                 fd=1
                 break
         if fd==0:
             raise forms.ValidationError("Password should contain atleast one number from 0-9!")
         return data
    
    def clean_confirm_password(self):
        data1 = self.cleaned_data.get('password')
        data = self.cleaned_data.get('confirm_password')

        if data != data1:
            raise forms.ValidationError("Doesn't match with the original password!")