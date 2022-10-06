from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "summary",
        "running_time",
    ]
    list_filter = [
        "running_time",
    ]
    search_fields = [
        "title",
    ]
