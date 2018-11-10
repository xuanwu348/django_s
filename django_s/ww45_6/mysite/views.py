from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from mysite import models

# Create your views here.
def index(request):
    template = get_template("index.html")
    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)

    """
    the second practise
    template = get_template('index.html')
    try:
        urid = request.GET['user_id']
        urpass = request.GET["user_pass"]
        byear = request.GET['byear']
        urfcolor = request.GET.getlist("fcolor")
    except:
        urid = None
    if urid is not None and len(urid) >=1 and urpass == "12345":
        verified = True
    else:
        verified = False
    years = range(1960,2021)
    html = template.render(locals())
    return HttpResponse(html)
    """

    """
    the first display
    template = get_template("index.html")
    return render(request=request, template_name="index.html")
    """
