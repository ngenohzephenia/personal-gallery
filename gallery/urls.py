from django.urls import path
from gallery.views import images,about,home,search_category
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('images/',images),
    path('search_category/', search_category, name="search_category"),
    path('media/path', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/path', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)