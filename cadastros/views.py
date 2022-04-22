from pyexpat import model
from django.shortcuts import render

from msilib.schema import Class
from re import template
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Igreja, Culto

from django.urls import reverse_lazy
class HomeView(TemplateView):
    template_name = 'paginas/home.html'



class IgrejaCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = u"adm"
    login_url = reverse_lazy('login')
    model = Igreja
    fields = ['nome','religiao','local']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-igreja')

class CultoCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Culto
    fields = ['nome_do_culto','descricao','data','igreja']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-culto')


"""------------Upgrade Igrejas e Cultos-------------------"""

class IgrejaUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    
    model = Igreja
    fields = ['nome','religiao','local']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-igreja')

class CultoUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')

    model = Culto
    fields = ['nome_do_culto','descricao','data','igreja']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-culto')




"""------------Deletar Igrejas e Cultos-------------------"""

class IgrejaDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Igreja
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-igreja')

class CultoDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Culto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-culto')

"""------------Lista Igrejas e Cultos-------------------"""

class IgrejaList(ListView):
    model = Igreja
    template_name = 'cadastros/lista/igreja-lista.html'

class CultoList(ListView):
    model = Culto
    template_name = 'cadastros/lista/culto-lista.html'
