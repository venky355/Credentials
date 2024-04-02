from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('uprec/<int:id>/', views.uprec, name='uprec'),
]
