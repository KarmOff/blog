from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from blog.models import *


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'user_name': auth.get_user(request)
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


def detail_article(request, article_id):
    user = auth.get_user(request)
    article = get_object_or_404(Article, pk=article_id)
    comment = Comments.objects.filter(article=article_id, user_comments=user)
    print(type(user))
    return render(request, 'blog/article.html', {'article': article, 'user':user, 'comment': comment})

