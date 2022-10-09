from django.contrib import admin
from .models import Review, MovieInfo


admin.site.register(
    [
        Review,
        MovieInfo,
    ]
)
