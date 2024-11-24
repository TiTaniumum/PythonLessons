from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from my_app.models import BBoard
from django.template import loader
from django.shortcuts import get_object_or_404
from my_app.forms import BBoardForm

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

def get_bboard(request: HttpRequest, bboard_id: int) -> HttpResponse:
    # bboard = BBoard.objects.get(id=bboard_id)
    # return HttpResponse(bboard.title)
    bboard = get_object_or_404(BBoard, id=bboard_id)
    # return HttpResponse(bboard.title)
    return render(request, "get_bboard.html", {"bboard": bboard})

def bboard_create(request: HttpRequest)-> HttpResponse:
    if(request.method == "POST"):
        form = BBoardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("New bboard has been saved")
    elif(request.method == "GET"):
        ...
    else :
        form = BBoardForm()
        return render(request, "bboard_create.html",{"form": form})