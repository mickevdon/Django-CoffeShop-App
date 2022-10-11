from django.urls import path

from .views import CoffeeListView, CoffeeDetailView

urlpatterns = [
    path("", CoffeeListView.as_view(), name="coffee_list"),
    path("<uuid:pk>/", CoffeeDetailView.as_view(), name="coffee_detail"),
]
