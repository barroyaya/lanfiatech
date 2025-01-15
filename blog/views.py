from django.shortcuts import render, get_object_or_404
from .models import Article

def blog_list(request):
    articles = Article.objects.order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'articles': articles})

def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/blog_detail.html', {'article': article})
