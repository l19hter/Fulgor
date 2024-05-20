from django.urls import path
from .views import catalog, show_product

app_name = 'onlineshop'

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('item/<int:id>/', show_product, name='show_product'),
]