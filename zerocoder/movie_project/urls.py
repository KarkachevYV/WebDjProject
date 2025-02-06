from django.urls import path
from . import views

urlpatterns = [
    path('', views.films, name='movie_project_films'),
    path('create_reviews/', views.create_reviews, name='add_reviews'),
    # path('data', views.data, name='page3'),
    # path('test', views.test, name='page4'),
    # другие маршруты
]