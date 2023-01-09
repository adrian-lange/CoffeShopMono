from rest_framework.viewsets import ModelViewSet
from authx.permissions import IsBaristaUser

from .serializers import (
    BaristaIngredientSerializer,
    ManagerIngredientSerializer,
)
from .models import Ingredient

from utils.mixins import CustomLoggingViewSetMixin


class IngredientViewSet(CustomLoggingViewSetMixin, ModelViewSet):

    queryset = Ingredient.objects.all()
    permission_classes = [IsBaristaUser]

    def get_serializer_class(self):
        if self.request.user.role > 2:
            return ManagerIngredientSerializer
        else:
            return BaristaIngredientSerializer
