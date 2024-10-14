from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class main_page(TemplateView):
    template_name = 'main.html'


class shop_page(TemplateView):
    template_name = 'shop.html'


class cart_page(TemplateView):
    template_name = 'cart.html'
