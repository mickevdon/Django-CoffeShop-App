from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q
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


class SearchResultsListView(ListView):
    model = Coffee
    context_object_name = "coffee_list"
    template_name = "coffee/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Coffee.objects.filter(
            Q(title__icontains=query) | Q(origin__icontains=query)
        )
