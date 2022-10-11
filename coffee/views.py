from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Coffee


class CoffeeListView(ListView):
    model = Coffee
    context_object_name = "coffee_list"
    template_name = "coffee/coffee_list.html"


class CoffeeDetailView(DetailView):
    model = Coffee
    context_object_name = "coffee"
    template_name = "coffee/coffee_detail.html"
