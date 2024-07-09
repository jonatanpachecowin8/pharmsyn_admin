from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('personal/', views.PersonalView.as_view(), name="personal"),
    path('personal/<int:personal_id>/', views.PersonalEditView.as_view(), name="editar_personal"),


    path('product/', views.ProductView.as_view(), name="product"),
    path('product/<str:product_id>/', views.ProductEditView.as_view(), name="editar_product"),


    path('inventory/', views.InventoryView.as_view(), name="inventory"),
    path('inventory/<str:inventory_id>/', views.InventarioEditView.as_view(), name="editar_inventory"),

]
