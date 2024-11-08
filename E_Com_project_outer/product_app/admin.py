from django.contrib import admin
from product_app.models import product_details
# Register your models here.

class product_detailsAdmin(admin.ModelAdmin):
    pass


admin.site.register(product_details, product_detailsAdmin)