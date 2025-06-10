from django.urls import path
from . import views

urlpatterns = [
    path('', views.relations, name='relations'),
    path('<slug:SLUG>', views.relations, name='slugSort'),
    path('unrelate/<int:id>', views.unrelate, name='unrelate'),
]