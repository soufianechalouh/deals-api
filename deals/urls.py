from rest_framework import routers

from deals.api.views import DealsViewSet, AllDealsViewSet, RecentDealsViewSet

router = routers.DefaultRouter()
router.register('deals', DealsViewSet, 'deals')
router.register('alldeals', AllDealsViewSet, 'deals')
router.register('recentdeals', RecentDealsViewSet, 'deals')

urlpatterns = router.urls

