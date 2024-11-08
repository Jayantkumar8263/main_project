from django.contrib import admin
from order_app.models import order_details, return_order

# Register your models here.
class order_detailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(order_details, order_detailsAdmin)


class return_orderAdmin(admin.ModelAdmin):
    pass
admin.site.register(return_order, return_orderAdmin)
