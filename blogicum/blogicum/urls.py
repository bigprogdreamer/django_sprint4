from django.contrib import admin
from django.urls import path, include
from core.views import internal_server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
]

handler500 = internal_server_error
