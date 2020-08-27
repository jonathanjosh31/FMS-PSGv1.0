"""fms_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user_interaction import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from devices.api import *
from user_interaction.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('useraccount/',include('user_interaction.urls')),
    path('doctorvisitor/',include('doctorvisitor.urls')),
    path('',views.root_front_page,name='root_front'),
    path('blogone/',views.blogone,name='blogone'),
    path('howitworks/',views.how_it_works,name='howitworks'),
    url(r'^api/student_list/$', StudentList.as_view(),name='Student_list'),
    url(r'^api/student_list/(.*)$', StudentDetail.as_view(),name='Student_Detail'),
    url(r'^api/device_list/$', DeviceList.as_view(),name='Device_list'),
    url(r'^api/device_list/(.*)$', DeviceDetail.as_view(),name='Device_Detail'),
    url(r'^api/visitor_list/$', VisitorList.as_view(),name='Visitor_list'),
    url(r'^api/visitor_list/(.*)$', VisitorDetail.as_view(),name='Visitor_Detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

