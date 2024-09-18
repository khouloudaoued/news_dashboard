from django.urls import path
from . import views

urlpatterns = [
    path('fetch-news/', views.fetch_news, name='fetch-news'),
]
