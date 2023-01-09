from rest_framework.viewsets import ModelViewSet
from authx.permissions import IsManagerUser
from .serializers import AdminSupplierSerializer
from .models import Supplier

from utils.mixins import CustomLoggingViewSetMixin


class SupplierViewSet(CustomLoggingViewSetMixin, ModelViewSet):

    queryset = Supplier.objects.all()
    permission_classes = [IsManagerUser]
    serializer_class = AdminSupplierSerializer
