from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'ACM_Wiki/site/UALR_ACM_Wiki.html')
