from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('create_news/', views.create_news, name='add_news'),
    # path('data', views.data, name='page3'),
    # path('test', views.test, name='page4'),
    # другие маршруты
]