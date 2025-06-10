from django.shortcuts import render
from django.views.generic.base import TemplateView
from CBV_app.models import mainModel
# Create your views here.
def Home(request):
    data = mainModel.objects.all()
    return render(request, 'home.html', {'data': data})

class Class_Based_Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = mainModel.objects.all()
        return context
