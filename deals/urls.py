from rest_framework import routers

from deals.api.views import DealsViewSet

router = routers.DefaultRouter()
router.register('deals', DealsViewSet, 'deals')

urlpatterns = router.urls

