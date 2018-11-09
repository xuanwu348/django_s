from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mysite import models

# Create your views here.

def index(request):
    product = models.Product.objects.all()
    template = get_template("index.html")
    html = template.render({"product":product})
    return HttpResponse(html)

def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    template = get_template("detail.html")
    html = template.render({"product":product,"images":images})
    return HttpResponse(html)
