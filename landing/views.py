from django.shortcuts import render

from .forms import SubscribersForm
from products.models import *


def landing(request):
    form = SubscribersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())



def home(request):
    products_Images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_Images_simulators = products_Images.filter(product__category__id=2)
    products_Images_MMORPG = products_Images.filter(product__category__id=1)
    return render(request, 'landing/home.html', locals())
