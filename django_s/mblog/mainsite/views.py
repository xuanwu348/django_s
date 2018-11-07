from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Post
from datetime import datetime

# Create your views here.

def homepage(request):
    """
    posts = Post.objects.all()
    post_list = []
    for i, post in enumerate(posts):
        post_list.append("No.{}&nbsp{}<br>".format(str(i), str(post)))
        post_list.append("<small>" + str(post.body) + "</small><br><br>")
    """
    template = get_template("index.html")
    posts = Post.objects.all()
    now = datetime.now()
    #html = template.render(locals())
    html = template.render({"posts":posts, "now":now})
    return HttpResponse(html)
