from django.contrib import admin
from .models import User,Posts
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username']

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']