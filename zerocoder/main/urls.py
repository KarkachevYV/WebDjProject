from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page1'),
    path('new', views.new, name='page2'),
    path('data', views.data, name='page3'),
    path('test', views.test, name='page4'),
    # другие маршруты
]