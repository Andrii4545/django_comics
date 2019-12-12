from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',hel),
    path('tags/',tags),
    path('such/',such),
    path('read/',glava),
    path('glava-read/',reads),
    path('logut/',logut),
    path('login/',login),
    path('coment/',add_coment),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
