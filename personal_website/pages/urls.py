from django.urls import path

from .views import fn,about_page

urlpatterns = [
    path("",fn),
    path("about/",about_page),
]
