from django.urls import path

from .views import CoffeeListView, CoffeeDetailView, SearchResultsListView

urlpatterns = [
    path("", CoffeeListView.as_view(), name="coffee_list"),
    path("<uuid:pk>/", CoffeeDetailView.as_view(), name="coffee_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
