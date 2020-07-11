from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentAccount
from .forms import raw_user_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def student_logout(request):
    logout(request)
    return redirect('/useraccount/studentlogin/')



def student_registration(request):
    
    if request.user.is_authenticated:
        logout(request)
        return redirect('/useraccount/studentlogin/')
    else:
    
        form = raw_user_form()
        if request.method == "POST" :
            form = raw_user_form(request.POST)


            if form.is_valid():
                save_obj = StudentAccount()
                save_obj.full_name = form.cleaned_data['full_name']
                save_obj.username = form.cleaned_data['roll_no']
                save_obj.management_name = form.cleaned_data['management_name']
                save_obj.contact_no = form.cleaned_data['contact_no']
                save_obj.department = form.cleaned_data['department']
                save_obj.residential_status = form.cleaned_data['residential_status']
                save_obj.email = form.cleaned_data['email']
                save_obj.set_password(form.cleaned_data['password'])
                save_obj.save()
                return redirect('/useraccount/thankyoupage/')
    
    return render(request,'user_interaction/student_registration_page.html',{'user_form': form })


def student_login(request):

    if request.user.is_authenticated:
        return redirect('/useraccount/studentlogin/')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')

            user = authenticate(request, username=username,password=password)
        
            if user is not None:
                login(request,user)
                return redirect('/useraccount/studentuser/')
            else:
                return redirect('/useraccount/studentregistration/')

    return render(request,'user_interaction/student_login_form.html')

@login_required(login_url = 'studentlogin')
def thank_you_page(request):
    return render(request,'user_interaction/thank_you_page.html')


@login_required(login_url = 'studentlogin')
def student_prof_page(request):
    
    curobj = StudentAccount.objects.get(username=request.user)
    user_dict = {
        'logged_student' :curobj,
    }
    return render(request,'user_interaction/student_prof.html',context=user_dict)

    