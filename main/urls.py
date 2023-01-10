from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import NewsAPI, NewsPUDAPI

urlpatterns = [
                  path('api/', NewsAPI.as_view(), name='create'),
                  path('api/<int:pk>', NewsPUDAPI.as_view(), name='update'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
