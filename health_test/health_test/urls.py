from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from . import settings
from core.sitemaps import TestSitemap


sitemaps = {
    'test': TestSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    # Все адреса с префиксом /auth
    # будут прернаправлены в модуль django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('tests.urls', namespace='tests')),
    path('account/', include('account.urls', namespace='account')),
    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        #document_root=settings.STATIC_ROOT,
        document_root=settings.STATICFILES_DIRS
    )
