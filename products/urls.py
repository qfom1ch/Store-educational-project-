from django.urls import path

from .views import IndexView, ProductsListView, basket_add, basket_remove

# from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('products/page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
