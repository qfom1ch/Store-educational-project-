from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, TemplateView

from common.views import TitleMixin

from .models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    context_object_name = "products"
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['category_id'] = self.kwargs.get('category_id')  # <-------------------------------
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def products(request, category_id=None, page_number=1):
#
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     paginator = Paginator(products, per_page=3)
#     products_paginator = paginator.page(page_number)
#     context = {'title': 'Store - Каталог',
#                'products': products_paginator,
#                'categories': ProductCategory.objects.all(),
#                }
#     return render(request, 'products/products.html', context)

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
