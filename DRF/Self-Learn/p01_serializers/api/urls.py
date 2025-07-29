from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListCreate.as_view()),
    path('books/json/', BookJsonResponse.as_view()),
    path('books/manualjson/', BookHttpJsonRenderer.as_view()),
    path('books/create/', BookCreateManual.as_view()),
    path('books/nested-create/', BookNestedCreate.as_view()),
    path('books/dynamic/', BookDynamicFields.as_view()),
]
