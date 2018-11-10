from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def index(request):
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
    the first display
    template = get_template("index.html")
    return render(request=request, template_name="index.html")
    """
