from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Films
from django.forms.models import model_to_dict
# import pdb


# pdb.set_trace()

def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def sign_in(request):
    return render(request, 'main/sign_in.html')


def films(request):
    films_list = Films.objects.all()[:20]
    return render(request, 'main/films.html', {'films_list': films_list})


def film(request, film_id):
    film_data = Films.objects.get(id=film_id)
    film_data = model_to_dict(film_data)
    return render(request, 'main/film.html', {'film_data': film_data})
