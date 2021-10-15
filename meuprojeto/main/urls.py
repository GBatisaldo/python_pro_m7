from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')), #main é o nome do diretório criado no comando startapp
    path('admin/', admin.site.urls),
]