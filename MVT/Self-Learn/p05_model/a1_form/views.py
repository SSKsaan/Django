from django.shortcuts import render
from . forms import apiForm

# Create your views here.
def Forms(request):
    return render(request, './a1_form/forms.html')

def formHtml(request):
    if request.method == "POST": # if not specifically checked here, the form will assumed as get method
        selected = request.POST.get("singleChoice")
        username = request.POST.get("name")
        return render(request, "./a1_form/form1_html.html", {"selected": selected, "username": username})
    return render(request, "./a1_form/form1_html.html")

def formDjango(request):
    if request.method == "POST":
        form = apiForm(request.POST, request.FILES)
        # request.POST stores the input data & request.FILES enables file storing
        print(form) # shows the WHOLE html code in console
        if form.is_valid(): # must need for using cleaned_data with request.POST
            print(form.cleaned_data) # only shows the inputs on console

            file = form.cleaned_data["file"] # accessing the uploaded file
            with open("./uploaded/" + file.name, 'wb+') as destination: # wb+ accepts all file types
                for chunk in file.chunks(): # chunk uses compressed files, so it's time efficient
                    destination.write(chunk) # storing uploaded file locally
    else:
        form = apiForm() # returning empty form
        
    return render(request, "./a1_form/form2_django.html", {"form": form})