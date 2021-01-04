from django.shortcuts import render
from django.views import View
from .services import repositorio

# Create your views here.

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        #print(request.GET.get('search'))
        print(repositorio(request.GET.get('search')))
        return render(request, self.template_name)
