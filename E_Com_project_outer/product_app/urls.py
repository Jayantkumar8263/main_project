from django.urls import path
from product_app.views import pro_home, del_a, up_a, view_cart, buy_now,cart

urlpatterns = [
    path('detail/<int:id>', pro_home, name = 'pro_home'), 
    path('del/<int:id>', del_a, name= 'delete'),
    path('update/<int:id>', up_a, name = 'update'),
    path("view_cart/", view_cart, name = 'view_cart'),
    path("cart/<int:id>", cart, name = 'cart'),
    path("buy_now/", buy_now, name = 'buy_now'),
]