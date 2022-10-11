from django.contrib import admin

from .models import Coffee


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")


admin.site.register(Coffee)
