from django.shortcuts import render
import requests
from django.http import JsonResponse
from newsapi import NewsApiClient

def fetch_news(request):
    
    newsApi = NewsApiClient(api_key='ceb2a687505b41f79df271d0b821bed0')
    
   
    headLines = newsApi.get_top_headlines(country='us')  
    
    articles = headLines['articles']
    
   
    
    desc = []
    news = []
    img = []

   
    for article in articles:
       
        desc.append(article.get('description', 'No description available'))
        news.append(article.get('title', 'No title'))
        img.append(article.get('urlToImage', 'No image available'))

    
    articles_list = zip( news, desc, img)
    
    
    return render(request, "main/index.html", context={"articles_list": articles_list})
