from django.contrib import admin
from django.urls import path,include
from core.views import frontpage ,aboutPage
urlpatterns = [
    path('', frontpage,name='frontpage'),
    path('aboutPage/', aboutPage,name='aboutPage'),

]
