from django.db import models

class Product(models.Model):  # Equivalent to 'prodmast'
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StockTransaction(models.Model):  # Equivalent to 'stckmain'
    TRANSACTION_TYPES = (('IN', 'Stock In'), ('OUT', 'Stock Out'))

    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    reference_note = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.reference_note}"

class StockDetail(models.Model):  # Equivalent to 'stckdetail'
    transaction = models.ForeignKey(StockTransaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
