from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>вцаукпегенкпаупкетыкеиы</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)>2020:
        # raise Http404
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>вцаукпегенкпаупкетыкеиы</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1> ')
