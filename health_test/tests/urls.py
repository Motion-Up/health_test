from unicodedata import name
from django.urls import path
from . import views


app_name = 'tests'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test_detail')
]
