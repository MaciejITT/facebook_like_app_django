from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user
from .models import Profile, FriendshipRelations
# Create your views here.


@login_required(login_url='login')
def home_page(request):
    friends = FriendshipRelations.objects.all()
    user = Profile.objects.get(user_id=request.user.id)
    friend_id_list = []
    friend_name = []
    for friend in friends:
        print(user.user_id, friend.user.first_name, friend.user_friend.id, friend.users_status)
        if user.user_id == friend.user.id and friend.users_status == 'friend':
            friend_name.append(friend.user_friend.first_name + ' ' + friend.user_friend.last_name)
            friend_id_list.append(friend.user_friend.id)
        if user.user_id == friend.user_friend.id and friend.users_status == 'friend':
            friend_name.append(friend.user.first_name + ' ' + friend.user.last_name)
            friend_id_list.append(friend.user.first_name + ' ' + friend.user.last_name)
    print(friend_id_list)
    context = {
        'friend_name': friend_name,
        'friend_id_list': friend_id_list,
    }

    return render(request, 'bookmate_app/home.html', context)


@unauthenticated_user
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


@unauthenticated_user
def sign_up_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='website_user')
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.sex = form.cleaned_data.get('sex')
            user.save()
            user.groups.add(group)
            messages.success(request, 'Account created')
            return redirect('login')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, "bookmate_app/signin.html", context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return render(request, 'bookmate_app/login.html')


@login_required(login_url='login')
def user_profile_page(request):
    user = Profile.objects.get(pk=request.user.pk)
    user_sex = user.sex
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    user_email = request.user.email

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'user_email': user_email,
        'user_sex': user_sex,
    }
    return render(request, 'bookmate_app/user_profile.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def statistics_page(request):
    return render(request, 'bookmate_app/statistics.html')


