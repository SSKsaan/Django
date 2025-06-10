from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def static(request):
    return render(request, 'myApp/static.html')
