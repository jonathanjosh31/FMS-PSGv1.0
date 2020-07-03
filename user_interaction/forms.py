from django import forms

from .models import user_detail,staff_user_detail


class raw_user_form(forms.Form):
    full_name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class' : 'form-control-lg form-control reginput','placeholder' : 'Full Name','id':'reginput'}))
    roll_no = forms.CharField(label='Roll No',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Roll No'}))
    management_name = forms.CharField(label='Management Name',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Management Name'}))
    contact_no = forms.DecimalField(max_digits=10, decimal_places=0,label='Contact No',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Contact No'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Email'}))
    residential_status = forms.CharField(label='Residential Status',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Residential Status'}))
    department = forms.CharField(label='Department',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Department'}))

class raw_staff_user_form(forms.Form):
    full_name = forms.CharField(label = 'Full Name',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Full Name'}))
    emp_id = forms.CharField(label = 'Employee ID',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Employee ID'}))
    management_name = forms.CharField(label = 'Management Name',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Management Name'}))
    contact_no = forms.DecimalField(label = 'Contact No',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Contact No'}))
    email = forms.EmailField(label = 'Email',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Email'}))
    residential_status = forms.CharField(label = 'Residential Status',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Residential Status'}))
    department = forms.CharField(label = 'Department',widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg','placeholder' : 'Department'}))



