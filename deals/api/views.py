from datetime import datetime, timedelta

from rest_framework import viewsets, permissions
from rest_framework.settings import api_settings

from deals.models import Deal
from deals.api.serializers import DealSerializer

from rest_framework_csv.renderers import CSVRenderer


class DealsViewSet(viewsets.ModelViewSet):
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    queryset = Deal.objects.exclude(category="unset")
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DealSerializer
    filterset_fields = ['category', 'store']


class AllDealsViewSet(DealsViewSet):
    queryset = Deal.objects.all()


class RecentDealsViewSet(DealsViewSet):
    def get_queryset(self):
        return Deal.objects.exclude(category="unset")\
            .exclude(thumbnail_url__isnull=True)\
            .exclude(thumbnail_url='')\
            .filter(last_update__gt=(datetime.now() - timedelta(minutes=5)))
