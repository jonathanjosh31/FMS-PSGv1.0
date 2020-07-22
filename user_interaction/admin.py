from django.contrib import admin
from .models import StudentAccount,Visitor,StudentEntryDetail
# Register your models here.
admin.site.register(StudentAccount)
admin.site.register(Visitor)
admin.site.register(StudentEntryDetail)