from django.shortcuts import render
from .models import Product
# Create your views here.

def showShop(request):
    context = {
        'title': 'Магазин',
        'products':  Product.objects.all(),
        'text_btn': 'Замовити',
    }
    if request.method == 'POST':
        product_id = request.POST.get('id')
        print(product_id)
    return render(request, 'shop.html', context)





def showBasket(request):
    context = {
        'title': 'Кошик'
    }
    return render(request, 'basket.html', context)