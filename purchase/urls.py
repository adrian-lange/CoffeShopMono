from django.urls.conf import include
from django.urls import re_path, path

from rest_framework.routers import DefaultRouter
from .viewsets import PurchaseViewSet
from .views import PurchaseListView, CancellingPurchase

router = DefaultRouter()

router.register(
    r'purchase',
    PurchaseViewSet,
    basename="purchase"
)

urlpatterns = [
    re_path(r'', include(router.urls)),
    path('purchase-list/',
         PurchaseListView.as_view(), name='purchase_list'),
    path('purchase-cancel/<int:pk>/', 
         CancellingPurchase.as_view(), name='purchase_cancel')
]
