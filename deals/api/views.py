from rest_framework import viewsets, permissions
from rest_framework.settings import api_settings

from deals.models import Deal
from deals.api.serializers import DealSerializer

from rest_framework_csv.renderers import CSVRenderer


class DealsViewSet(viewsets.ModelViewSet):
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    queryset = Deal.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DealSerializer
    filterset_fields = ['category', 'store']
