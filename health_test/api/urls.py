from django.urls import include, path
from rest_framework import routers
from api import views


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'tests', views.TestViewSet)
router.register(r'results', views.ResultsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
        )
    ),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
