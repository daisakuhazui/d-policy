from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('radmin/', admin.site.urls),
    path(r'', include('blog.urls')),
]
