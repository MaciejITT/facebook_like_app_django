from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home_page(request):
    return render(request, 'base.html')


def login_page(request):
    return render(request, "bookmate/login.html")


def signin_page(request):
    form = UserCreationForm()
    context ={
        'form': form,
    }
    return render(request, "bookmate/signin.html", context)

