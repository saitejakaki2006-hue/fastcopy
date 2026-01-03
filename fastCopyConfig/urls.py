from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.admin import admin_site  # Import your custom admin instance

# 🗺️ SEO: Sitemap Configuration
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
from core.views import robots_txt

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # 🛠️ Custom Admin Site
    path('admin/', admin_site.urls),
    
    # 🏠 Core App URLs
    path('', include('core.urls')),
    
    # 🗺️ SEO: Sitemap & Robots.txt
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]

# 📂 Serve Media Files (PDFs/Images) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)