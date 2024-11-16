from django.db import models

# Create your models here.

class product_details(models.Model):
    name = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)
    quantity = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    descount_price = models.CharField(max_length = 250)
    descount_percent = models.CharField(max_length = 250)
    on_scale = models.CharField(max_length = 250)
    images = models.FileField(upload_to='None', max_length=100)
    card = models.ForeignKey("product_details", on_delete=models.CASCADE, null=True, blank=True)
    
    
class add_to_cart(models.Model):
    user = models.ForeignKey("customer_app.custom_user", on_delete=models.CASCADE)
    product = models.ForeignKey("product_app.product_details", on_delete=models.CASCADE)

class buy_now(models.Model):
    user = models.ForeignKey("customer_app.custom_user", on_delete=models.CASCADE)
    product = models.ForeignKey("product_app.product_details", on_delete=models.CASCADE)
