
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from book.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
