from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    data={"title": "Medical","title1": "Sistema Medico Online"}
    #return HttpResponse("<h1>Pantalla de Inicio<h1>")
    #return JsonResponse(data)
    return render(request, 'core/home.html', data)