from .models import Category, MenuItem, OrderModel
from django.contrib import admin

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)