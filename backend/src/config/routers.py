from rest_framework import routers

import marking.views
import patients.views

category_router = routers.SimpleRouter()
category_router.register("category", marking.views.CategoryViewSet)

tag_router = routers.SimpleRouter()
tag_router.register("tag", marking.views.TagViewSet)

patients_router = routers.SimpleRouter()
patients_router.register("patients", patients.views.PatientsViewSet)
