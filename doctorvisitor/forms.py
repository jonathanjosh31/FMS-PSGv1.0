from django import forms
from .models import Doctor

class doctor_reg_form(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control input-border-bottom','id' : 'inputFloatingLabel'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control input-border-bottom','id' : 'inputFloatingLabel'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control input-border-bottom','id' : 'inputFloatingLabel'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control input-border-bottom','id' : 'inputFloatingLabel'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control input-border-bottom','id' : 'inputFloatingLabel'}))