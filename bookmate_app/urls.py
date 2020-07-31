from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('signin/', views.sign_up_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home_page, name='home'),
]
