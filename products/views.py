from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from users.models import User

def index(request):
    context = {
        'title': 'Index',

    }
    return render(request, 'products/index.html', context)

def catalog(request, category_id=None):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    context = {
        'title': 'Catalog',
        'products': products,
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/catalog.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


