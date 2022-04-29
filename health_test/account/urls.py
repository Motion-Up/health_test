from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<slug:test_slug>/', views.get_results, name='get_results'),
    path(
        '<slug:test_slug>/delete/<int:result_id>/',
        views.delete_result,
        name='delete_result'
    ),
    path(
        '<slug:test_slug>/change/<int:result_id>/',
        views.edit_result,
        name='edit_result'
    ),
]
