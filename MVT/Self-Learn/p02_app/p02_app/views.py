# This file is not automatically created by default, unlike others
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1 style="text-align:center;">Project is Working</h1>')