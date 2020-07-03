from django.urls import path
from . import views

urlpatterns = [
    path('prof_page/',views.index,name='index'),
    path('studentuserform/',views.user_page,name='user_form'),
    path('staffuserform/',views.staff_user_page,name='staff_user_form'),
    path('thankyoupage/',views.thank_you_page,name='thank_you_page')
]