from django.urls import path
from . import views

urlpatterns = [
    path('fetch-news/', views.fetch_news, name='fetch-news'),  # ربط الفيو الخاص بجلب الأخبار
    path('', views.fetch_news, name='home'),  # جعل الصفحة الرئيسية تظهر الأخبار
]
