from django.contrib import admin

from .models import (
    Category, Comment, Review, Title, Genre
)

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
