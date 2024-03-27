from django.contrib import admin
from .models import Category, Customer ,Product , order ,date

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(order)
admin.site.register(date)