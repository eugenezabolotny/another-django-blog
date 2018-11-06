from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def details(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'details.html', {'article': article})
