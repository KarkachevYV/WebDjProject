from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('main.urls')),  # Подключение URL из приложения
    path('', include('main.urls')),
    path('news', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
