from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def home_page(request):
    return render(request, 'bookmate_app/home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, "bookmate_app/login.html")


def sign_up_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.sex = form.cleaned_data.get('sex')
            user.save()
            messages.success(request, 'Account created')
            return redirect('login')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, "bookmate_app/signin.html", context)


def logout_user(request):
    logout(request)
    return render(request, 'bookmate_app/login.html')
