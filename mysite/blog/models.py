from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title
