from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from deals.models import Deal
from deals.api.serializers import DealSerializer


class DealsViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DealSerializer
    filterset_fields = ['category', 'store']
