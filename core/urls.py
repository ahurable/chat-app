
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home_url'),
    path('account/', include('account.urls', namespace='account'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)