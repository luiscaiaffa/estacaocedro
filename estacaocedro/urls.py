from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap, index
from django.conf.urls.static import static
from django.conf import settings
from .sitemaps import *

sitemaps = {
	'static':StaticViewSitemap,
	'noticia':NoticiaSitemap,
	'galeria':GaleriaSitemap
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', index, {'sitemaps':sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    url(r'^', include('apps.website.urls', namespace='website')),
    url(r'^painel/', include('apps.painel.urls', namespace='painel')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)