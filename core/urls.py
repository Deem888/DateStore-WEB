from django.contrib import admin
from django.urls import path,include
from core.views import frontpage ,aboutPage,yourDates
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', frontpage,name='frontpage'),
    path('aboutPage/', aboutPage,name='aboutPage'),
    path('yourDates/',yourDates,name='yourDates'),
]

