from core.models.personal.rol import Rol
from core.models.personal.privilegio import Privilegio
from core.models.personal.personal import Personal
from core.models.personal.rol_privilegio import RolPrivilegio
from core.models.personal.branch import Branch
from core.models.personal.laboratory import Laboratory


from core.models.cliente.user import User

from core.models.ventas.order import Order

from core.models.product.product import Product
from core.models.product.category import Category
from core.models.product.product_attribute import ProductAttribute

from core.models.inventario.product_variation import ProductVariation
from core.models.inventario.inventory_movement import InventoryMovement


__all__=[
    Laboratory,
    User,
    Order,
    Rol,
    Privilegio,
    Personal,
    RolPrivilegio,
    Branch,
    Product,
    ProductAttribute,
    ProductVariation,
    InventoryMovement,
    Category
]