from rest_framework.routers import DefaultRouter

from notes.views import NotesViewSet

router = DefaultRouter()
router.register(r"notes", NotesViewSet, basename="note")

urlpatterns = router.urls
