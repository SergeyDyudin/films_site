from django.shortcuts import render, get_object_or_404
from .models import Films
from django.forms.models import model_to_dict


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
    film_data = get_object_or_404(Films, id=film_id)
    # film_data = model_to_dict(film_data)
    return render(request, 'main/film.html', {'film_data': film_data})
