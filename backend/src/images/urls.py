from rest_framework.routers import DefaultRouter

from images.views import ImageViewSet, TilesViewSet

router = DefaultRouter()
router.register(r"images", ImageViewSet, basename="image")
router.register(r"tiles", TilesViewSet, basename="tile")

urlpatterns = router.urls
