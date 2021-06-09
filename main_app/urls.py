from django.urls import path
from . import views

from .views import Home, InventoryList, InventoryCreate, InventoryDelete, InventoryDetail, InventoryUpdate, SignUp

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('inventory/', InventoryList.as_view(), name="inventory_list"),
    path('inventory/new', InventoryCreate.as_view(), name="inventory_create"),
    path('inventory/<int:pk>/', InventoryDetail.as_view(), name="inventory_detail"),
    path('inventory/<int:pk>/update', InventoryUpdate.as_view(), name="inventory_update"),
    path('inventory/<int:pk>/delete', InventoryDelete.as_view(), name="inventory_delete"),
    path('accounts/signup/', SignUp.as_view(), name="signup")
    # what .as_view?
    # path('accounts/profile/', SignUp.as_view(), name="profile")
]
