from urllib import response
from django.shortcuts import get_object_or_404, render, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles)
    return Response(serializer.data)

def article_detail(request, aarticle_pk):
    article = get_object_or_404(Article, article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)