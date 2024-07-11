from django.urls import path
from .views import HomeView
from .views import PersonalView
from .views import PersonalEditView
from .views import ProductView
from .views import ProductEditView
from .views import InventoryView
from .views import InventarioEditView
from .views import HistoryView
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('personal/', PersonalView.as_view(), name="personal"),
    path('personal/<int:personal_id>/', PersonalEditView.as_view(), name="editar_personal"),


    path('product/', ProductView.as_view(), name="product"),
    path('product/<str:product_id>/', ProductEditView.as_view(), name="editar_product"),
    path('product/add', ProductView.as_view(), name="add_product"),


    path('inventory/', InventoryView.as_view(), name="inventory"),
    path('inventory/<str:inventory_id>/', InventarioEditView.as_view(), name="editar_inventory"),

    path('historial/', HistoryView.as_view(), name="historial"),

    # Auth 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout')
]
