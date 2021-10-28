from django.urls import path
from .views import home, product_detail, edit_product

urlpatterns = [
    path('', home),
    path('detail/<id>', product_detail),
    path('edit/<pk>', edit_product),
]