from django.contrib import admin
from .models import Category,Food,Accounts

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','food_name','price','description','image','cat_fk']

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['cardno','cvv','expiry','balance']

admin.site.register(Food,FoodAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Accounts,AccountsAdmin)

