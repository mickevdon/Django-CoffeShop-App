from urllib import response
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Coffee, Review


class CoffeeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",
        )
        cls.coffee = Coffee.objects.create(
            title="Delicious Coffee",
            origin="UK",
            price="10.00",
        )

        cls.review = Review.objects.create(
            coffee=cls.coffee,
            author=cls.user,
            review="Good review",
        )

    def test_coffee_listing(self):
        self.assertEqual(f"{self.coffee.title}", "Delicious Coffee")
        self.assertEqual(f"{self.coffee.origin}", "UK")
        self.assertEqual(f"{self.coffee.price}", "10.00")

    def test_coffee_list_view(self):
        response = self.client.get(reverse("coffee_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delicious Coffee")
        self.assertTemplateUsed(response, "coffee/coffee_list.html")

    def test_coffee_detail_view(self):
        response = self.client.get(self.coffee.get_absolute_url())
        no_response = self.client.get("coffee/12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Delicious Coffee")
        self.assertContains(response, "Good review")
        self.assertTemplateUsed(response, "coffee/coffee_detail.html")
