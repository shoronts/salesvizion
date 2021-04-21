from django.contrib import admin
from .models import news


@admin.register(news)
class UserAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')
    fields = ('title', 'slug', 'date', 'FetcheredPicture', 'NewsDescriptions')