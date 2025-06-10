from django.shortcuts import render, redirect
from .models import relationModel, exampleModel
from .forms import Relation_Form

# Create your views here.

def relations(request, SLUG = None):
    data = relationModel.objects.all() # for passing all object data to the template
    if request.method == "POST":
        form = Relation_Form(request.POST) # getting form with entries
        if form.is_valid():
            form.save() # saving the form entry into the database
            return redirect('relations')
    else:
        form = Relation_Form()

    if SLUG is not None: # in function None is passed if no SLUG is specified
        sort = exampleModel.objects.get(slug=SLUG) # getting the object with the specified slug
        data = relationModel.objects.filter(example=sort) # filtering a field with specific value
        # 'slug' & 'example' aren't keywords, but required field names

    return render(request, './a3_relation/relations.html', {'form': form, 'data': data})

def unrelate(request, id):
    relationModel.objects.get(pk=id).delete()
    return redirect('relations')