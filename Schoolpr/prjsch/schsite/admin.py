from django.contrib import admin
from django.contrib.auth.models import User
from .models import kolUrok, Teachers, Students, Items, Klass, Password1
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(kolUrok)
admin.site.register(Teachers)


    
admin.site.register(Students)
admin.site.register(Items)
admin.site.register(Klass)
admin.site.register(Password1)
admin.site.site_title = "RealAdmin"
admin.site.site_header = "РиальнаяАдминка"