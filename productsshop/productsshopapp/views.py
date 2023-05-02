
from django.shortcuts import render
from .models import Product

# Create your views here.

def showShop(request):
    context = {
        'title': 'Магазин',
        'products':  Product.objects.all(),
        'text_btn': 'Замовити',
    }

    response = render(request, 'shop.html', context)

    if request.method == 'POST':

        basket = request.COOKIES.get('cart', None)
        product_id = request.POST.get('id')
        
        count_basket_products = request.COOKIES.get('count', None)
        get_count_product = request.POST.get('count')

        print(get_count_product)

        if basket != None:
            basket_list = basket.split(' ')
            count_basket_products_list =  count_basket_products.split(' ')

            if product_id in basket_list:
                #pass
                index_product = basket_list.index(product_id)
                count_basket_products_list[index_product] = get_count_product
                response.set_cookie('count', ' '.join(count_basket_products_list))
            else:
                response.set_cookie('cart', basket+' '+product_id)
                response.set_cookie('count', count_basket_products+' 1')
        else:
            response.set_cookie('cart', product_id)
            response.set_cookie('count', get_count_product)
            
    return response





def showBasket(request):
    context = {
        'title': 'Кошик'
    }
    return render(request, 'basket.html', context)