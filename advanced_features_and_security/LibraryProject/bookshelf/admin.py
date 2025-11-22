from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter= ('title', 'author', 'publication_year')
    search_fields= ('title', 'author', 'publication_year')

class CustomUserAdmin(admin.ModelAdmin):
    list_filter= ('username', 'email', 'first_name', 'last_name', 'date_of_birth')
    search_fields= ('username', 'email', 'first_name', 'last_name', 'date_of_birth')
    

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)