from django.shortcuts import render
from django.views.generic import View, TemplateView
# from django.http import HttpResponse

# Create your views here.
#python **kwargs key word arguments, will accept any number of arguments for a dictionary/hash map
# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context



# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS!")



# def index(request):
#     return render(request, 'index.html')
