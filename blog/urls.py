from django.contrib import admin
from django.urls import path
from .models import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_site, name='blog_site'),
]