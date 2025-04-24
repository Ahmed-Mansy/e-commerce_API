from django.urls import path,include
from . import views

urlpatterns = [
    path('products/',views.get_all_product,name='products'),
    path('products/<str:pk>/',views.get_product_by_id,name='get_product_by_id')    

]
