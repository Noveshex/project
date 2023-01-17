from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class HomePage(ListView):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'object'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Main page of the website'
        return ctx
