from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from authx.permissions import IsCashierUser
from .serializers import (
    CreatePurchaseOrderSerializer,
    PurchaseOrderSerializer
)

from .models import PurchaseOrder

from utils.mixins import CustomLoggingViewSetMixin


class PurchaseViewSet(
    CustomLoggingViewSetMixin,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = PurchaseOrder.objects.all()
    permission_classes = [IsCashierUser]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return CreatePurchaseOrderSerializer
        else:
            PurchaseOrderSerializer
