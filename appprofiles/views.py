from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .services import profiles, repositories
from django.http.response import HttpResponse

# Create your views here.

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        print(repositories(request.GET.get('search')))
        if repositories(request.GET.get('search')) == 0:
            return HttpResponse("Sem repositorio")
        return render(request, self.template_name,{'profile':profiles(request.GET.get('search')),
        'repository':repositories(request.GET.get('search'))})

