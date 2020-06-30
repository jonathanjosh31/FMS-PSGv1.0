from django.shortcuts import render
from django.http import HttpResponse
from .models import user_detail
# Create your views here.

def index(request):
    curobj = user_detail.objects.filter(user_name__exact='jonathanjosh31')
    my_dict = {'full_name' : curobj[0].full_name,'user_name' : curobj[0].user_name,'management_name' : curobj[0].management_name,'contact_no' : curobj[0].contact_no,'email' : curobj[0].email,'designation' : curobj[0].designation,'department' : curobj[0].department}
    return render(request,'user_interaction/index1.html',context=my_dict)

def user_page(request):
    return render(request,'user_interaction/user_form.html')
