from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentAccount,StudentEntryDetail
from .forms import raw_user_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


######################################## Custom Functions for Views ################################################



# ################################################# Views for Root ############################################################
def root(request):
    return render(request,'root.html')

def root_front_page(request):
    return render(request,'frontroot.html')

def how_it_works(request):
    return render(request,'works.html')

def blogone(request):
    return render(request,'blog1.html')


def student_logout(request):
    logout(request)
    return redirect('/useraccount/studentlogin/')



def student_registration(request):
    
    if request.user.is_authenticated:
        return redirect('/useraccount/studentuser/')
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
                save_obj.batch_year = form.cleaned_data['batch_year']
                save_obj.set_password(form.cleaned_data['password'])
                save_obj.save()
                return redirect('/useraccount/thankyoupage/')
    
    return render(request,'user_interaction/student_registration_page.html',{'user_form': form })


def student_login(request):
    incorrect = ''
    if request.user.is_authenticated:
        return redirect('/useraccount/studentuser/')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')

            user = authenticate(request, username=username,password=password)
        
            if user is not None:
                login(request,user)
                return redirect('/useraccount/studentuser/')
            else:
                incorrect = 'Incorrect username or password'

    return render(request,'user_interaction/student_login_form.html',{ 'message' : incorrect })


def thank_you_page(request):
    return render(request,'user_interaction/thank_you_page.html')


@login_required(login_url = 'studentlogin')
def student_prof_page(request):
    
    curobj = StudentAccount.objects.get(username=request.user)
    pos = curobj.email.find("@")
    email_name = str(curobj.email[0:pos])
    email_domain = str(curobj.email[pos:len(curobj.email)])


    user_dict = {
        'logged_student' :curobj,
        'emailname' : email_name,
        'emaildomain' : email_domain
    }
    return render(request,'user_interaction/student_prof_new.html',context=user_dict)

def entriespage(request):
    
    userentry = StudentEntryDetail.objects.get(account=request.user)
    entrydetail = userentry.entries
    context = {
          'user_entry' : entrydetail,
      }

    return render(request,'user_interaction/entries.html',context)

def statschart(request):
    return render(request,'user_interaction/stats_chart.html')