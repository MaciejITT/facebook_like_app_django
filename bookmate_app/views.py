from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.


def start_page(request):
    return render(request, 'base.html')


def home_page(request):
    return render(request, 'bookmate_app/home.html')


def login_page(request):
    return render(request, "bookmate_app/login.html")


def sign_up_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("ok")
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.sex = form.cleaned_data.get('sex')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        print("nie ok")
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, "bookmate_app/signin.html", context)

