from django.contrib import admin
from .models import question, answer


admin.site.register(question)
admin.site.register(answer)