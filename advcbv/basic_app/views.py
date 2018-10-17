from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'




# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS!")



# def index(request):
#     return render(request, 'index.html')
