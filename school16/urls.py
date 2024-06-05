from django.contrib import admin
from django.urls import path
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.postdetail, name="postdetail"),
]
