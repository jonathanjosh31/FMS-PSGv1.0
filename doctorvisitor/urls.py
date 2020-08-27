from django.urls import path
from . import views

urlpatterns = [
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('doctorloginform/',views.doctorloginform,name='doctorloginform'),
    path('doctorregform/',views.doctorregform,name='doctorregform'),
    path('doctorpage/',views.doctor_page,name='doctorpage'),
    path('visitorstoday/',views.visitors_today,name='visitorstoday'),
    path('patiententrytable/',views.entries_page,name='patiententrytable')
]