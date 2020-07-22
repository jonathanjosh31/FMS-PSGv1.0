
from rest_framework import serializers
from .models import StudentAccount,Visitor

# Serializing the models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAccount
        fields = ('username','email','joined_date','last_login',
        'is_admin','is_active','is_superuser','is_staff','management_name',
        'full_name','contact_no','department','residential_status')

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('timestamp','image','temperature')