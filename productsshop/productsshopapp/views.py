
from django.shortcuts import render
from .models import Product
import json

# Create your views here.

def showShop(request):
    context = {'title': 'Магазин','text_btn': 'Замовити',}
    product_list_for_html = [{'product': product, 'amount': 1} for product in Product.objects.all()]

    if request.COOKIES.get('basket'):
        basket_value = json.loads(request.COOKIES.get('basket'))
        for check_product in product_list_for_html:
            for check_product_basket in basket_value:
                if check_product_basket['product']['id_product'] in  str(check_product['product'].pk):
                    check_product['amount'] = check_product_basket['product']['amount']
    context['products'] = product_list_for_html
    response = render(request, 'shop.html', context)


    if request.method == 'POST':
        get_product_id = request.POST.get('id')
        get_product_amount = request.POST.get('amount')
        basket_cookie = request.COOKIES.get('basket', None)
        if basket_cookie: 
            basket_cookie = json.loads(basket_cookie)
            for product_from_basket in basket_cookie:
                if get_product_id in product_from_basket['product']['id_product']:
                    product_from_basket['product']['amount'] = get_product_amount
                    break
            else:
                product_dict = {'product':{"id_product": get_product_id, "amount": get_product_amount}}
                basket_cookie.append(product_dict)
        else:
            basket_cookie = []
            product_dict = {'product':{"id_product": get_product_id, "amount": get_product_amount}}
            basket_cookie.append(product_dict)

        response.set_cookie('basket', json.dumps(basket_cookie))
    return response



def showBasket(request):
    context = {
        'title': 'Кошик'
    }
    return render(request, 'basket.html', context)



