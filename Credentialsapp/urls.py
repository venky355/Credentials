from django.urls import path
from . import views  # Correct import statement

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('user/', views.user_home, name='user_home'),
    path('dealer/', views.dealer_home, name='dealer_home'),
    path('user/register/', views.user_registration, name='user_registration'),
    path('dealer/register/', views.dealer_registration, name='dealer_registration'),
    path('login/', views.user_login, name='login'),
]

