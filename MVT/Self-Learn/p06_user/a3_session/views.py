from django.shortcuts import render

# Create your views here.
def session(request):
    return render(request,'session.html')

def set_session(request):
    request.session['code'] = '1XS0l' # setting a key-value pair to session
    data = {
        'id': 23,
        'name': 'test'
    }
    request.session.update(data) # updating a dictionary in session
    print(request.session.get_session_cookie_age()) # session expiration in seconds
    print(request.session.get_expiry_date()) # session expiration date & time
    return render(request,'set_session.html')

def get_session(request):
    #* session data is by default hashed for security purposes
    ID = request.session.get('id') # getting a session value by key
    code = request.session.get('code', 'UNKNOWN') # setting a default value if key doesn't exist
    request.session.modified = True # resets the expiration timer(set in settings.py) on refresh
    return render(request, 'get_session.html', {'code':code, 'ID':ID})

def del_session(request):
    # del request.session['code'] # deleting a specific session value by key
    request.session.flush() # deleting all session values
    return render(request, 'del_session.html')