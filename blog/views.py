from django.shortcuts import render, get_object_or_404
from .models import Article
import markdown
# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'articles': articles})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    return render(request, 'blog/detail.html', context={'article':article})
