from django.urls import path
from customer_app.views import home, registration, ulogin, ulogout, profile
from customer_app.views import delete_data,update_data, bank_details
from customer_app.models import custom_user
urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('login/', ulogin, name='login'),
    path('logout/', ulogout, name = 'logout'),
    path('profile/<int:i>', profile, name='profile'),
    path('del/<int:id>', delete_data, name= 'delete'),
    path('update/<int:id>', update_data, name = 'update'),
    path('bank_details', bank_details,name = 'bank_details'),
]