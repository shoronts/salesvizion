from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class news(models.Model):
        FetcheredPicture = models.ImageField(default='news.png', upload_to='News Pictures')
        title = models.CharField(max_length=250)
        slug = models.SlugField(blank=True, null=True)
        date = models.DateTimeField(default=timezone.now)
        NewsDescriptions = RichTextUploadingField(blank=True, null=True)

        def get_absolute_url(self):
            return f'/news/{self.slug}/'

        def snippet(self):
            return self.NewsDescriptions[:250] + '.....'

        def __str__(self):
            return self.title