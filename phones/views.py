from django.shortcuts import render, redirect
from.models import Phone  

from django.http import HttpResponse


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET['sort']
    if sort =='max_price':
        phones_all = Phone.objects.all().order_by('-price')
    elif sort == 'min_price':
        phones_all = Phone.objects.all().order_by('price')
    elif sort == 'name':
        phones_all = Phone.objects.all().order_by('name')
    else:
        phones_all = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)



    
