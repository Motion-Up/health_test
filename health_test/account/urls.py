from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<slug:test_slug>/', views.get_results, name='get_results')
]
