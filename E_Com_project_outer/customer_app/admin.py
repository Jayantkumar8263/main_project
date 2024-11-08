from django.contrib import admin
from customer_app.models import custom_user, bank_details
# Register your models here.


admin.site.register(custom_user)


class bank_detailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(bank_details, bank_detailsAdmin)