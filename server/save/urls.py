from rest_framework import routers
from .views import SaveViewSet

router = routers.DefaultRouter()
router.register(r'saves', SaveViewSet, basename="saves")

urlpatterns = router.urls