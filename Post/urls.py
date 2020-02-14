from django.urls import path
from . import views

# /posts
urlpatterns = [
  path('Post/',views.index),
]