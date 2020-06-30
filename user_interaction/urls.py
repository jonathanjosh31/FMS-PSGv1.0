from django.urls import path
from . import views

urlpatterns = [
    path('prof_page',views.index,name='index'),
    path('userform',views.user_page,name='user_form')
]