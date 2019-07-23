from django.urls import path

from article.views import home,article
app_name = 'article'
urlpatterns = [
   path('',home,name='home'),
   path('article/',article,name='article'),
]
