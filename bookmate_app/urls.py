from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='base'),
    path('login/', views.login_page, name='login'),
    path('signin/', views.sign_up_page, name='signin'),
    path('home/', views.home_page, name='home'),
]
