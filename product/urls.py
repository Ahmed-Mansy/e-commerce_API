from django.urls import path,include
from . import views

urlpatterns = [
    path('products/',views.get_all_product,name='products'),
   
]
