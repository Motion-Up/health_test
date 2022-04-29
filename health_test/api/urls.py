from django.urls import include, path
from rest_framework import routers
from api import views


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tests', views.TestViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
        )
    ),
]