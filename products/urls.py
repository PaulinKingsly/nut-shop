from django.urls import path
from . import views

from products.views import catalog, index, basket_add, basket_remove
app_name = 'products'

urlpatterns = [
    # path('index', views.index, name='Index'),
    # path('catalog', views.catalog, name='Catalog'),

    path('catalog/', catalog, name='catalog'),
    path('index/', index, name='index'),
    path('category/<int:category_id>', catalog, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')

]
