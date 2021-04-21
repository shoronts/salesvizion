from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


class question(models.Model):
    question = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, null=True, max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/question/{self.slug}/'

    def __str__(self):
        return self.question

class answer(models.Model):
    user = models.CharField(max_length=100)
    examDate = models.CharField(max_length=100)
    examVersion = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, null=True, max_length=500)
    date = models.DateTimeField(default=timezone.now)
    firstAnswer = models.TextField(max_length=1000)
    secondAnswer = models.TextField(max_length=1000)
    thirdAnswer = models.TextField(max_length=1000)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/result/{self.slug}/'

    def __str__(self):
        return self.user
