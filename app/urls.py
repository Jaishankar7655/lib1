from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('books/new-books/', addbook, name='addbooks'),
    path('' , main, name='main'),
    path('success/' , success, name='success'),
    path('allbooks/' , allbooks, name='allbooks'),
    path('viewbook/<int:pk>' , viewbook, name='viewbook'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


