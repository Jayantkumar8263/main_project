from django.db import models

# Create your models here.

class order_details(models.Model):
    order_no = models.ForeignKey("order_details", on_delete=models.CASCADE)
    user_id = models.CharField(max_length = 50)
    product = models.CharField(max_length = 50)
    total_prise = models.CharField(max_length = 50)
    payment = models.CharField(max_length = 50)
    shypping_address = models.CharField(max_length = 50)
    order_status = models.CharField(max_length = 50)
    
class return_order(models.Model):
    order_no = models.ForeignKey("return_order", on_delete=models.CASCADE)
    reason_for_return = models.TextField(max_length = 1000)
    
    
    
    
    