from django.contrib import admin
from rest_framework.authtoken import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("book.urls")),
    path('login/', views.obtain_auth_token)
]
