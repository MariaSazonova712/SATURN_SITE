from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.db.models import Q


class ProductListView(ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'


def search_results(request):
    query = request.GET.get('query')
    if query:
        query_lower = query.lower()
        products = Product.objects.filter(
            Q(name__icontains=query_lower) |
            Q(name__icontains=query_lower.replace(' ', '')) |
            Q(name__istartswith=query_lower) |
            Q(name__icontains=query)
        ).distinct()
    else:
        products = Product.objects.all()

    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'main/search_results.html', context)


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})
