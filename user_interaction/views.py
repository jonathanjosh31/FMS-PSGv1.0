from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_detail,staff_user_detail
from .forms import raw_user_form,raw_staff_user_form
# Create your views here.

def index(request):
    curobj = user_detail.objects.filter(roll_no__exact='jonathanjosh31')
    my_dict = {'full_name' : curobj[0].full_name,'roll_no' : curobj[0].roll_no,'management_name' : curobj[0].management_name,'contact_no' : curobj[0].contact_no,'email' : curobj[0].email,'residential_status' : curobj[0].residential_status,'department' : curobj[0].department}
    return render(request,'user_interaction/index1.html',context=my_dict)

def user_page(request):
    form = raw_user_form()   #get method by default 
    if request.method == "POST" :
        form = raw_user_form(request.POST)
        if form.is_valid():
            save_obj = user_detail()  #model object
            save_obj.full_name = form.cleaned_data['full_name']
            save_obj.roll_no = form.cleaned_data['roll_no']
            save_obj.management_name = form.cleaned_data['management_name']
            save_obj.contact_no = form.cleaned_data['contact_no']
            save_obj.email = form.cleaned_data['email']
            save_obj.residential_status = form.cleaned_data['residential_status']
            save_obj.department = form.cleaned_data['department']
            save_obj.save()
            return redirect('/userdetails/thankyoupage/')
            # correct data so save it in the database
    return render(request,'user_interaction/user_form.html',{'user_form' : form })

def staff_user_page(request):
    form = raw_staff_user_form()
    if request.method == "POST" :
        form = raw_staff_user_form(request.POST)
        if form.is_valid():
            save_obj = staff_user_detail() #staff model object
            save_obj.full_name = form.cleaned_data['full_name']
            save_obj.emp_id = form.cleaned_data['emp_id']
            save_obj.management_name = form.cleaned_data['management_name']
            save_obj.contact_no = form.cleaned_data['contact_no']
            save_obj.email = form.cleaned_data['email']
            save_obj.residential_status = form.cleaned_data['residential_status']
            save_obj.department = form.cleaned_data['department']
            print(save_obj.full_name)
            save_obj.save()
            return redirect('/userdetails/thankyoupage/')
    return render(request,'user_interaction/staff_user_form.html',{'user_form' : form })

def thank_you_page(request):
    return render(request,'user_interaction/thank_you_page.html')

def root_page(request):
    return render(request,'user_interaction/index.html')


    

