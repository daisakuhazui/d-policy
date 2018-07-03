from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostIndex.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
]
