from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome),
    path('tempLang/', views.tempLang, name='tempLang'),
    path('URLtag/', views.URLtag, name='URLtag'),
    path('urltag/<int:id>/', views.urltag, name='urltag'), #must have .../urltag/anyINT/ to access
]