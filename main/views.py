from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.http import is_safe_url
from django.conf import settings

from .forms import LoginForm
from .models import Films


@login_required
def home(request):
    return render(request, 'main/index.html')


@login_required
def about(request):
    return render(request, 'main/about.html')


@login_required
def contacts(request):
    return render(request, 'main/contacts.html')


def sign_in(request):
    if request.user.is_authenticated:
        HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    # return HttpResponseRedirect(reverse('home'))
                    redirect_to = request.GET.get('next', '/')
                    if is_safe_url(url=redirect_to, allowed_hosts=settings.ALLOWED_HOSTS):
                        return HttpResponseRedirect(redirect_to)
                else:
                    messages.error(request, 'Username or password is incorrect')
        else:
            form = LoginForm(initial={'username': '', 'password': ''})
        return render(request, 'main/sign_in.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('sign-in'))


@login_required
def films(request):
    films_list = Films.objects.all().order_by('id')
    paginator = Paginator(films_list, 28)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/films.html', {'page_obj': page_obj})
    # return render(request, 'main/films.html', {'films_list': films_list})


@login_required
def film(request, film_id):
    film_data = get_object_or_404(Films, id=film_id)
    # film_data = model_to_dict(film_data)
    return render(request, 'main/film.html', {'film_data': film_data})
