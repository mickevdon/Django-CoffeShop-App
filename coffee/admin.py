from django.contrib import admin

from .models import Coffee, Review


class ReviewInline(admin.TabularInline):
    model = Review


class CoffeeAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "origin",
        "price",
    )


admin.site.register(Coffee, CoffeeAdmin)
