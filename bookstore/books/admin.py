from django.contrib import admin
from .models import Products


from .models import Category
admin.site.register(Category)
# Register your models here.

from .models import Comment
admin.site.register(Comment)


# class Product_Admin(admin.ModelAdmin):
#     search_fields = (
#         'title',
#     )
#     list_filter = [
#         'category',
#         'status'
#     ]
#     list_display = ['title', 'price', 'amount']
#     list_per_page = 2
#
#
# admin.site.register(Products, Product_Admin)


class Product_Admin(admin.ModelAdmin):
    list_display = ('category', 'author',)
    list_filter = ('characteristic',)

admin.site.register(Products, Product_Admin)