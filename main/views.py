from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from forms import LoginForm
from .models import Films



def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

@login_required
def contacts(request):
    return render(request, 'main/contacts.html')


def sign_in(request):
    if request.method == 'POST':
        # Создаем экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('home'))
    else:
        pass
    return render(request, reverse('sign-in'))
    # return render(request, 'main/sign_in.html')


def films(request):
    films_list = Films.objects.all()
    paginator = Paginator(films_list, 28)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/films.html', {'page_obj': page_obj})
    # return render(request, 'main/films.html', {'films_list': films_list})


def film(request, film_id):
    film_data = get_object_or_404(Films, id=film_id)
    # film_data = model_to_dict(film_data)
    return render(request, 'main/film.html', {'film_data': film_data})
