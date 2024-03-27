from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)

# admin.site.register(Category)

# admin.site.register(House)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title")

admin.site.register(Category, CategoryAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display = ("id","title", "productCategory", "area", "address", "price","status")
    list_editable = ("status",)

admin.site.register(House, HouseAdmin)