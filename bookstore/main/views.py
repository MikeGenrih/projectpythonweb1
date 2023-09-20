

from django.shortcuts import render
import random
from books.models import Products, Category


def main(request):
    all_products = Products.objects.all()
    if all_products.exists():
        random_product = random.choice(all_products) ##### ---->>>>> choise random
    else:
        return render(request, 'main/main sight.html',)
    context = {
        'random_product': random_product,
    }
    return render(request, 'main/main sight.html', context)
########################################################################


def about(request):
    return render(request, 'main/about us.html')

def contacts(request):
    return render(request, 'main/contacts.html')