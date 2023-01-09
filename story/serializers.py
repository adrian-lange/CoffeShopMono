from rest_framework.serializers import ModelSerializer, SlugRelatedField
#from rest_framework import serializers
from .models import Ingredient
from supplier.serializers import (
    AdminSupplierSerializer
)


class BaseIngredientSerializer(ModelSerializer):
    #unit = serializers.CharField(source='get_unit_display')

    class Meta:
        model = Ingredient
        fields = '__all__'


class BaristaIngredientSerializer(BaseIngredientSerializer):
    supplier = SlugRelatedField(
        read_only=True,
        slug_field='custom_id'
    )


class ManagerIngredientSerializer(BaseIngredientSerializer):
    supplier = AdminSupplierSerializer()
