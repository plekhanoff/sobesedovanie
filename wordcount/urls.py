from django.urls import path
from . import views


urlpatterns = [
    path('', views.load_file, name='load'),
    path('wordcount/', views.word_count, name='wordcount'),
    path('clear_memory/', views.clear_memory, name='clear_memory'),
]
