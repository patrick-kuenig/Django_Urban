from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def function_test(request):
    return render(request, 'function.html')


class ClassTest(TemplateView):
    template_name = 'class.html'