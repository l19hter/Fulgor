from django.shortcuts import render

from .models import Product

def catalog(request):
    products = Product.objects.all()
    title = 'Каталог магазина "Фулгор"'
    return render(request, 'index.html', {'products': products,
                                          'title': title})

def show_product(request, id):
    product = Product.objects.get(pk=id)
    title = product.name
    return render(request, 'item.html', {'product' : product,
                                         'title': title})


