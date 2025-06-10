from django.shortcuts import render
from . import models, forms

from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
def Home(request):
    data = models.myModel.objects.all()
    return render(request, 'home.html', {'data': data})


class Create(CreateView):
    model = models.myModel # associated model to be used
    form_class = forms.myForm # associated form to be passed
    template_name = 'form.html' # render destination
    success_url = reverse_lazy('home') # works like return redirect


class Update(UpdateView):
    model = models.myModel 
    form_class = forms.myForm
    template_name = 'form.html' 
    success_url = reverse_lazy('home') 
    pk_url_kwarg = 'id' # to pass the id of the object in url
    
    # def form_valid(self, form): # only here for request.FILES
    #     form.instance.pic = self.request.FILES.get('pic')
    #     return super().form_valid(form)


class Delete(DeleteView):
    model = models.myModel 
    template_name = 'delete.html' # needs to submit a POST form
    success_url = reverse_lazy('home') 
    pk_url_kwarg = 'id' 
    # DeleteView class provides self.object as the object to be deleted