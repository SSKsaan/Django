from django.shortcuts import render
import datetime

# Create your views here.
def appHome(request):
    return render(request, "myApp/home.html")

def tempLang(request):
    # Context (passing something from backend to frontend):
    data = {
        'Name' : 'San', 'Age' : 21,
        'Dict' : [
            {'id':1, 'Title':'Python'},
            {'id':2, 'Title':'HTML'}
        ],
        'Datetime' : datetime.datetime.now(),
        'Birthday' : datetime.date(year=2003, month=3, day=20)
    }
    return render(request, "myApp/tempLang.html", data) # passing context
    # can be passed as a key-value pair (dictionary)
    # return render(request, "myApp/tempLang.html", context={'Name' : 'San', 'Age' : 21})

    
def URLtag(request):
    return render(request, "myApp/URLtag.html", {'input' : request.GET})
    # passes input as dict IF anything GOT after .../utag/? as url input (optional)

def urltag(request, id):
    return render(request, "myApp/URLtag.html", {'id' : id})
    # passed the id recieved from urls to html page


