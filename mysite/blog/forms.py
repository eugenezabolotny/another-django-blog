from django import forms

from .models import Article
from ckeditor_uploader.fields import RichTextUploadingFormField


class NewArticleForms(forms.ModelForm):
    description = RichTextUploadingFormField

    class Meta:
        model = Article
        fields = ['title', 'description']
