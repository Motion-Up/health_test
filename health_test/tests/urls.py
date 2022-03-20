from django.urls import path
from . import views


app_name = 'tests'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<slug:test_slug>/', views.test_detail, name='test_detail'),
]
