from django.shortcuts import render
from django.views import View
from .services import profiles, repositories

# Create your views here.

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        #print(request.GET.get('search'))
        print(repositories(request.GET.get('search')))
        return render(request, self.template_name,{'profile':profiles(request.GET.get('search')),
        'repository':repositories(request.GET.get('search'))})
