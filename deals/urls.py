from rest_framework import routers

from deals.api.views import DealsViewSet, AllDealsViewSet

router = routers.DefaultRouter()
router.register('deals', DealsViewSet, 'deals')
router.register('alldeals', AllDealsViewSet, 'deals')

urlpatterns = router.urls

