from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Doctor,VisitorsToday
from .forms import doctor_reg_form
# Create your views here.

def doctorlogin(request):
    
    return render(request,'doctorvisitor/doctorlogin.html')

def doctorloginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/useraccount/thankyoupage/')

    return render(request,'doctorvisitor/doctorloginform.html')

def doctorregform(request):
    form = doctor_reg_form()
    if request.method == 'POST':
        form = doctor_reg_form(request.POST)
        if form.is_valid():
            save_obj = Doctor()
            save_obj.username = form.cleaned_data['username']
            save_obj.email = form.cleaned_data['email']
            save_obj.password = form.cleaned_data['password']
            save_obj.name = form.cleaned_data['full_name']
            save_obj.contact_no = form.cleaned_data['contact_no']
            save_obj.save()
    return render(request,'doctorvisitor/doctorregform.html',{'form' : form})

def doctor_page(request):
    
    curobj = Doctor.objects.get(username='1011')
    pos = curobj.email.find("@")
    email_name = str(curobj.email[0:pos])
    email_domain = str(curobj.email[pos:len(curobj.email)])

    user_dict = {
        'doctor' :  curobj,
        'emailname' : email_name,
        'emaildomain' : email_domain,

    }
    return render(request,'doctorvisitor/doctorpage.html',context=user_dict)

def visitors_today(request):

    completed=[]
    pending=[]
    curobj = Doctor.objects.get(username='1011')
    entryobj = VisitorsToday.objects.get(account=curobj)
    for i in entryobj.entries:
        if i['status'] == True:
            completed.append(i)
        else:
            pending.append(i)
    com_len = len(completed)
    pen_len = len(pending)

    context = {
        'completed' : completed,
        'pending' : pending,
        'comlen' : com_len,
        'penlen' : pen_len, 
    }

    return render(request,'doctorvisitor/doctor_visitor_page.html',context)

def entries_page(request):
    doctor = Doctor.objects.get(username='1011')
    entry = VisitorsToday.objects.get(account=doctor)
    entrydetail = entry.entries
    context = {
          'user_entry' : entrydetail,
      }
    return render(request,'doctorvisitor/entriestable.html',context)