from django.urls import path
from . import views

urlpatterns = [
    path('', views.Forms, name='forms'),
    path('html/', views.formHtml, name='form1'),
    path('django/', views.formDjango, name='form2'),
]