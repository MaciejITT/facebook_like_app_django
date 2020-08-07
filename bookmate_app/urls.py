from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_page, name='login'),
    path('signin/', views.sign_up_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home_page, name='home'),
    path('statistics/', views.statistics_page, name='statistics'),
    path('profile/', views.user_profile_page, name='profile'),
    path('profile/edit/', views.update_user_data, name='update_user'),
    path('change-password/', views.change_password, name='change_password'),
    path('./', views.invitations_from_users, name='invitations')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
