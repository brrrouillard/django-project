from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"), # Homepage
    path('about', views.about, name="about")
]