from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from my_app.models import BBoard
from django.template import loader

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('index.html')
    ads = BBoard.objects.all()
    context = {"ads": ads}
    return HttpResponse(template.render(context, request))
    # text = "content content"
    # for obj in BBoard.objects.all():
    #     text+= obj.title + " " + str(obj.published) + "\n"
    # return HttpResponse(text, content_type = "text/plain; charset=utf-8")
    #return HttpResponse("Hello World")