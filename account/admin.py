
from django.contrib import admin
from .models import User
 
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','email','is_active','is_google')