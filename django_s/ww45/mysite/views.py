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
