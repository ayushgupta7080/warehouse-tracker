from django.contrib import admin
from .models import Product, StockMain, StockDetail

admin.site.register(Product)
admin.site.register(StockMain)
admin.site.register(StockDetail)
