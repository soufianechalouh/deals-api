from django.urls import path
from rest_framework import routers
from . import views

from deals.api.views import DealsViewSet

router = routers.DefaultRouter()
router.register('deals', DealsViewSet, 'deals')

urlpatterns = [
    path('csv_deals', views.get_deals, name='deals-csv')
]
urlpatterns += router.urls

