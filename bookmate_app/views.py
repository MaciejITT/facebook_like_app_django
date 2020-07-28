from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.


def home_page(request):
    return render(request, 'base.html')


def login_page(request):
    return render(request, "bookmate/login.html")


def sign_up_page(request):
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, "bookmate/signin.html", context)

