from django.shortcuts import render
from article.models import Article
# Create your views here.

def home(request):
    print(request.user)
    return render(request,'article/home.html')

def article(request):
    
    article = Article.objects.all().order_by('-create_at')
    context = {
        'article':article
    }
    return render(request,'article/article.html',context)
