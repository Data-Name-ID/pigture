from rest_framework.routers import DefaultRouter

from patients.views import PatientsViewSet

router = DefaultRouter()
router.register(r"patients", PatientsViewSet, basename="patient")

urlpatterns = router.urls
