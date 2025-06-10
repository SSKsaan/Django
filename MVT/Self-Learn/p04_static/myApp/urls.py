from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('STATIC/', views.static, name='static'),
]