from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import main,closed
# from .views import ItemListAPIView,ItemAPIView

urlpatterns = [
    path('',  main ,name = 'main' ),
    # path('',  closed ,name = 'closed' ),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)