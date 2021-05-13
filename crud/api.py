from rest_framework import routers
from education import api_views

router = routers.DefaultRouter()
router.register(r"student", api_views.StudentViewSet)
router.register(r"class", api_views.ClassViewSet)

