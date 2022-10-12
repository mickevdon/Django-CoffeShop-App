from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Coffee


class CoffeeListView(LoginRequiredMixin, ListView):
    model = Coffee
    context_object_name = "coffee_list"
    template_name = "coffee/coffee_list.html"
    login_url = "account_login"


class CoffeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Coffee
    context_object_name = "coffee"
    template_name = "coffee/coffee_detail.html"
    login_url = "account_login"
    permission_required = "coffee.special_status"
