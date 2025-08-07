from django.db import models

class Product(models.Model):
    product_code = models.CharField(max_length=10, unique=True)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_code} - {self.product_name}"

class StockMain(models.Model):
    date = models.DateField(auto_now_add=True)
    reference_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.reference_no} ({self.date})"

class StockDetail(models.Model):
    stock_main = models.ForeignKey(StockMain, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"
