from time import perf_counter
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Coffee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    front_picture = models.ImageField(upload_to="front_picture/", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can access all types of coffee"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("coffee_detail", args=[str(self.id)])


class Review(models.Model):
    coffee = models.ForeignKey(
        Coffee,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=300)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
