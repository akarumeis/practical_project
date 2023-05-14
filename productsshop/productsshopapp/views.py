
from django.shortcuts import render
from .models import Product
from itertools import zip_longest
import json

# Create your views here.


def showShop(request):
    context = {'title': 'Магазин', 'text_btn': 'Замовити', }
    product_list_for_html = [{'product': product, 'amount': 1}
                             for product in Product.objects.all()]

    if request.COOKIES.get('basket'):
        basket_value = json.loads(request.COOKIES.get('basket'))
        for check_product in product_list_for_html:
            for product_from_basket in basket_value:
                if product_from_basket['product']['product_id'] in str(check_product['product'].pk):
                    check_product['amount'] = product_from_basket['product']['amount']
    context['products'] = product_list_for_html

    response = render(request, 'shop.html', context)

    if request.method == 'POST':
        product_id = request.POST.get('product')
        amount = request.POST.get('amount')
        product_list = []

        if request.COOKIES.get('basket'):
            basket_value = json.loads(request.COOKIES.get('basket'))
            for obj_from_basket in basket_value:
                if product_id in obj_from_basket['product']['product_id']:
                    obj_from_basket['product']['amount'] = amount
                    break
            else:
                product_dict = {'product': {
                    'product_id': product_id, 'amount': amount, }}
                basket_value.append(product_dict)
            product_list = basket_value
        else:
            product_dict = {'product': {
                'product_id': product_id, 'amount': amount, }}
            product_list.append(product_dict)
        response.set_cookie('basket', json.dumps(product_list))

    return response


def showBasket(request):
    context = {
        'title': 'Кошик',
        'text_btn': 'Delete'
    }

    if request.COOKIES.get('basket'):
        basket_cookie = json.loads(request.COOKIES.get('basket', None))
        for change_product in basket_cookie:
            change_product['product']['product_id'] = Product.objects.get(
                pk=change_product['product']['product_id'])
        context['products'] = basket_cookie

    response = render(request, 'basket.html', context)

    if request.method == 'POST':
        if request.COOKIES.get('basket'):

            get_product_id = request.POST.get('id')
            basket_cookie = json.loads(request.COOKIES.get('basket', None))

            if request.POST.get('button') == 'delete':
                for change_product in basket_cookie:
                    if get_product_id in change_product['product']['product_id']:
                        basket_cookie.pop(basket_cookie.index(change_product))

            elif request.POST.get('button') == 'change_amount':
                get_product_amount = request.POST.get('amount')
                for change_product in basket_cookie:
                    if get_product_id in change_product['product']['product_id']:
                        change_product['product']['amount'] = get_product_amount

            response.set_cookie('basket', json.dumps(basket_cookie))

    return response
