from django.contrib import admin
from django.urls import path,include
from core.views import frontpage
urlpatterns = [
    path('admin/', admin.site.urls),
        path('', frontpage,name='frontpage'),

]
