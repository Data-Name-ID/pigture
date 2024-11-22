from rest_framework import routers

import marking.views


category_router = routers.SimpleRouter()
category_router.register(r"category", marking.views.CategoryViewSet)

tag_router = routers.SimpleRouter()
tag_router.register(r"tag", marking.views.TagViewSet)