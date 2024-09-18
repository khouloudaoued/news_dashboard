from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('news/', include('news.urls')),  # الربط مع urls الخاصة بتطبيق الأخبار
    path('admin/', admin.site.urls),      # صفحة الأدمن
]

# إضافة دعم الملفات الثابتة في حال وجودها
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
