from django.urls import path
from . import views

urlpatterns = [
    path('studentregistration/',views.student_registration,name='studentregistration'),
    path('studentlogin/',views.student_login,name='studentlogin'),
    path('thankyoupage/',views.thank_you_page,name='thankyoupage'),
    path('studentlogout/',views.student_logout,name='studentlogout'),
    path('studentuser/',views.student_prof_page,name='studentuser'),
    path('studententry/',views.entriespage,name='studententry')
]