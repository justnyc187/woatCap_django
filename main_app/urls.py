from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('inventory/', views.InventoryList.as_view(), name="inventory_list"),
    path('inventory/new', views.InventoryCreate.as_view(), name="inventory_create"),
    path('inventory/<int:pk>/', views.InventoryDetail.as_view(), name="inventory_detail"),
    path('inventory/<int:pk>/update', views.InventoryUpdate.as_view(),
         name="inventory_update")
]
