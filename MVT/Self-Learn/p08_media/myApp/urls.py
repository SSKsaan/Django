from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:id>', views.Update.as_view(), name='update'),
    path('delete/<int:id>', views.Delete.as_view(), name='delete'),
]