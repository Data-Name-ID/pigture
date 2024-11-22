from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar.toolbar

    urlpatterns += debug_toolbar.toolbar.debug_toolbar_urls()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
