from typing import ContextManager
from django.shortcuts import render
from .models import FavMovie, ProjetoDjango
# Create your views here.

def homepage(request):
    return render(
                    request=request,
                    template_name="home.html",
                    context={"cursos": ProjetoDjango.objects.all}
    )

def homepage(request):
    return render(
                    request=request,
                    template_name="home.html",
                    context={"filmes": FavMovie.objects.all}
    )