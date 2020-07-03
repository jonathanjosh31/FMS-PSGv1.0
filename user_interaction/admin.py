from django.contrib import admin
from .models import user_detail,staff_user_detail
# Register your models here.
admin.site.register(user_detail)
admin.site.register(staff_user_detail)