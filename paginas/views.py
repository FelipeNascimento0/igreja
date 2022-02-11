from django.shortcuts import render

from django.views.generic import TemplateView





class HomeView(TemplateView):
    template_name = 'paginas/home.html'

class QuemSomosView(TemplateView):
    template_name = 'paginas/quem_somos.html'