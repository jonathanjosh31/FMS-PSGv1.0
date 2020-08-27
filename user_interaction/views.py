from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentAccount,StudentEntryDetail,StudentMedicalReport
from .forms import raw_user_form,medical_report_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from user_interaction.custom_functions import monthlyChart,yearlyChart,pieChart,get_total_average_temp
import datetime,calendar

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
                save_obj_entry = StudentEntryDetail()
                save_obj_med = StudentMedicalReport()
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
                save_obj_entry.account = save_obj
                save_obj_entry.save()
                save_obj_med.account1 = save_obj
                save_obj_med.save()
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
    
    f=0
    today_date = datetime.datetime.now()
    no_entry_str = ''
    recent_entry_temp = []
    recent_entry_date = []
    curobj = StudentAccount.objects.get(username=request.user)
    pos = curobj.email.find("@")
    email_name = str(curobj.email[0:pos])
    email_domain = str(curobj.email[pos:len(curobj.email)])

    curentryobj = StudentEntryDetail.objects.get(account=request.user)
    total_entries = len(curentryobj.entries)
    if len(curentryobj.entries) != 0:
        avgTemp = get_total_average_temp(curentryobj.entries)
    else:
        avgTemp = 'No entries till now'
    if len(curentryobj.entries) >= 5:
        recent_entries = curentryobj.entries[len(curentryobj.entries)-5:len(curentryobj.entries)]
        f=1
    elif len(curentryobj.entries) == 0:
        no_entry_str = 'No Entries till now'
    else:
        recent_entries = curentryobj.entries
        f=1
    if f==1:
        for i in recent_entries:
            recent_entry_temp.append(i['Temp'])
            recent_entry_date.append(i['Day'])

    if len(curentryobj.entries) != 0:
        lastentry = curentryobj.entries[len(curentryobj.entries)-1]
        lastentry_month = calendar.month_name[lastentry['Month']]
    else:
        lastentry_month = 'No Entries'

    user_dict = {
        'logged_student' :curobj,
        'emailname' : email_name,
        'emaildomain' : email_domain,
        'total_entries' : total_entries,
        'avg_temp' : avgTemp,
        'recent_temp' : recent_entry_temp,
        'recent_day' : recent_entry_date,
        'noentry' : no_entry_str,
        'lastentrymonth' : lastentry_month
    }
    return render(request,'user_interaction/student_prof_new.html',context=user_dict)

@login_required(login_url = 'studentlogin')
def entriespage(request):
    
    userentry = StudentEntryDetail.objects.get(account=request.user)
    entrydetail = userentry.entries
    context = {
          'user_entry' : entrydetail,
      }

    return render(request,'user_interaction/entries.html',context)

@login_required(login_url = 'studentlogin')
def statschart(request):

    userstats = StudentEntryDetail.objects.get(account = request.user)
    monthlystats = monthlyChart(userstats.entries)
    yearlystats = yearlyChart(userstats.entries)
    piestats = pieChart(userstats.entries)


    monthlyday = []
    monthlytemp =[]
    for i in monthlystats:
        monthlyday.append(i[0])
        monthlytemp.append(i[1])

    context = {
        'monthlyday' : monthlyday,
        'monthlytemp' : monthlytemp,
        'yearly' : yearlystats,
        'pie' : piestats, 
    }

    return render(request,'user_interaction/stats_chart.html',context)

@login_required(login_url = 'studentlogin')
def medicalReport(request):

    med_form = medical_report_form()
    if request.method == "POST" :
            med_form = medical_report_form(request.POST)

            if med_form.is_valid():
                save_obj  = StudentMedicalReport.objects.get(account1=request.user)
                date_obj = datetime.date.today()
                date = str(date_obj.year) + '-' + str(date_obj.month) + '-' + str(date_obj.day)
                report_entry = {'diabetes' : med_form.cleaned_data['diabetes'] , 'pulmonary_diseases' : med_form.cleaned_data['pulmonary_diseases'] , 'high_low_pressure' : med_form.cleaned_data['high_low_pressure'],'respiratory_diseases':med_form.cleaned_data['respiratory_diseases'],'any_other':med_form.cleaned_data['any_other'],'contact30':med_form.cleaned_data['contact30'],'diagnose30':med_form.cleaned_data['diagnose30'],'visit10':med_form.cleaned_data['visit10'],'fever':med_form.cleaned_data['fever'],'dry_cough':med_form.cleaned_data['dry_cough'],'breathing_prob':med_form.cleaned_data['breathing_prob'],'sore_throat':med_form.cleaned_data['sore_throat'],'date' : date}
                save_obj.medical_reports.append(report_entry)
                save_obj.save()
                return redirect('/useraccount/studentuser/')
    context = {
        'report' : med_form,
    }

    return render(request,'user_interaction/medical_report.html',context)

def medical_reports_show(request):

    med_reports = StudentMedicalReport.objects.get(account1=request.user)
    preexisting = {}
    recent_last_couple_days = {}
    if len(med_reports.medical_reports) !=0 :
        preexisting = med_reports.medical_reports[0]
        recent_last_couple_days = med_reports.medical_reports[len(med_reports.medical_reports)-1]

    context = {
        'last_couple' : recent_last_couple_days,
        'preexisting' : preexisting,
    }

    return render(request,'user_interaction/medical_report_show.html',context)

def doctor_visitor_page(request):
    return render(request,'user_interaction/doctor_visitor_page.html')
