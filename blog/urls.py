from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='Home-Blog'),
    path('home.html', views.blog, name='Home-Blog'),
    path('about.html', views.about, name='A propos'),
    path('article.html', views.article, name='Articles')
]

