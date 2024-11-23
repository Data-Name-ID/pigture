from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

import config.routers
import images.urls

API_PREFIX = "api/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(images.urls)),
    path(API_PREFIX, include(config.routers.category_router.urls)),
    path(API_PREFIX, include(config.routers.tag_router.urls)),
    path(API_PREFIX, include(config.routers.patients_router.urls)),
]


if settings.DEBUG:
    import debug_toolbar.toolbar

    urlpatterns += debug_toolbar.toolbar.debug_toolbar_urls()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
