from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 3
    
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "crud/product_detail.html"
    
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix ='_update_form'
    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('list')
    
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
class LogoutVIew(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'
    