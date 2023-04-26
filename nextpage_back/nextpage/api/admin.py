from django.contrib import admin
from .models import Category, Book
# admin.site.register(Category)
# admin.site.register(Book)
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title')