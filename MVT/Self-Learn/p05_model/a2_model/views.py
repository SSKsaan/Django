from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

def Models(request):
    data = models.myModel.objects.all() # for passing all object data to the template
    form = forms.Model_Form()
    return render(request, './a2_model/models.html', {'data': data, 'form': form})

def add(request):
    if request.method == "POST":
        form = forms.Model_Form(request.POST) # getting form with entries
        if form.is_valid():
            form.save() # saving the form entry into the database
            return redirect('models')
    else:
        form = forms.Model_Form()
    return render(request, './a2_model/update_model.html', {'form': form})


def delete(request, id):
    models.myModel.objects.get(pk=id).delete() # deletes the specified object
    return redirect('models')


def edit(request, id):
    data = models.myModel.objects.get(pk=id) # getting the object with the specified id
    if request.method == "POST":
        form = forms.Model_Form(request.POST, instance=data) # getting form with entries & instance
        if form.is_valid():
            form.save()
            return redirect('models')
    else:
        form = forms.Model_Form(instance=data)  # getting the form with just the object data
    return render(request,'./a2_model/update_model.html', {'form': form})

