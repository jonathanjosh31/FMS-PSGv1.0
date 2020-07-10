from django.urls import path
from . import views

urlpatterns = [
    path('studentregistration/',views.student_registration,name='studentregistration'),
    path('studentloginform/',views.student_login,name='studentlogin'),
    path('thankyoupage/',views.thank_you_page,name='thankyoupage')
]