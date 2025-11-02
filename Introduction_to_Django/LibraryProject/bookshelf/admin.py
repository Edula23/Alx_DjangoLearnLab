from django.contrib import admin
from .models import Book

# Simple registration: shows the model in the admin site with default options
admin.site.register(Book)

# Example: a more useful registration with a custom ModelAdmin
# Uncomment and adjust if you want a list display, search, or filters
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "published_year")
#     search_fields = ("title", "author")
#     list_filter = ("published_year",)
