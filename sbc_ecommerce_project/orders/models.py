from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Order({self.customer_name} - {self.product_name})"

