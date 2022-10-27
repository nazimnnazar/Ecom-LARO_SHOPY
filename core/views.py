from math import prod
from django.shortcuts import render
from.models import*
from core.models import products
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# Create your views here.
def home(request,c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.all().filter(available=True)
    cat = categ.objects.all()
    return render(request, 'product.html', {'pr': prodt, 'ct': cat})

def views(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'views.html',{'pr':prod})

def signup(request):
    return render(request,'signup.html')
