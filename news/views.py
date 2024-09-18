import requests
from django.http import JsonResponse
from .models import Article

def fetch_news(request):
    api_key = 'ceb2a687505b41f79df271d0b821bed0'  
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    # Fetch data from the external news API
    response = requests.get(url)
    api_data = response.json()
    
    # Retrieve articles from the database
    articles = Article.objects.all()
    
    # Convert database articles into a list of dictionaries
    articles_list = list(articles.values('title', 'description', 'url', 'published_at'))
    
    # Combine API data and database articles in the response
    return JsonResponse({
        'api_articles': api_data.get('articles', []),  # Extract 'articles' from API response
        'db_articles': articles_list
    })
