from core.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class SuperUser(UserAdmin):
    ordering=['id']

admin.site.register(User, SuperUser)