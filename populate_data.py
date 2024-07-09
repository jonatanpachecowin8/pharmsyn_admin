from core.models.personal.rol import Rol
from core.models.personal.privilegio import Privilegio
from core.models.personal.personal import Personal
from core.models.personal.rol_privilegio import RolPrivilegio
from core.models.personal.branch import Branch

from core.models.personal.laboratory import Laboratory

from core.models.product.product import Product
from core.models.product.product_attribute import ProductAttribute
from core.models.product.category import Category

from core.models.inventario.product_variation import ProductVariation
from core.models.inventario.inventory_movement import InventoryMovement
from django.shortcuts import get_object_or_404


def populate_data():
    
    branch1 = Branch.objects.create(
        name="Sucursal Principal",
        address="Avenida Roca Y Coronado, 181"
    )
    
    branch2 = Branch.objects.create(
        name="Sucursal 2 Agoto",
        address="Bibosi, Santa Cruz de la Sierra"
    )
    
    # Crear marcas (Brand)
    brand1 = Laboratory.objects.create(
        id="2",
        name="Laboratorio Chile",
        image="https://emhvpljjyqwgxxtsiylw.supabase.co/storage/v1/object/public/public/sw2_crm/brands/logo_lab_chile.png?t=2024-06-23T17%3A27%3A27.255Z",
        is_featured=False,
        product_count=150
    )
    
    brand2 = Laboratory.objects.create(
        id="3",
        name="Portugal",
        image="https://emhvpljjyqwgxxtsiylw.supabase.co/storage/v1/object/public/public/sw2_crm/brands/logo_porutgal.png",
        is_featured=True,
        product_count=200
    )
    
    # Crear categorías (Category)
    category1 = Category.objects.create(
        id="1",
        name="Medicamento",
        unit_of_measure="gr"
    )
    
    category2 = Category.objects.create(
        id="2",
        name="Producto de Belleza",
        unit_of_measure="ml"
    )
    
    # Crear productos (Product)
    product1 = Product.objects.create(
        id="6676e6fad91161434cdd4f69",
        stock=150,
        price=25.0,
        sale_price=30.0,
        title="Benzaclin",
        thumbnail="https://emhvpljjyqwgxxtsiylw.supabase.co/storage/v1/object/public/public/sw2_crm/products/Benzaclin.jpg",
        product_type="drug",
        laboratory=brand1,
        description="hives; difficulty breathing; swelling of your face...",
        category=category1
    )
    
    product2 = Product.objects.create(
        id="6676e6fad91161434cdd4",
        stock=200,
        price=35.0,
        sale_price=40.0,
        title="Tetracycline",
        thumbnail="https://emhvpljjyqwgxxtsiylw.supabase.co/storage/v1/object/public/public/sw2_crm/products/Tetracycline_.jpeg",
        product_type="drug",
        laboratory=brand2,
        description="Used for the treatment of various infections...",
        category=category2
    )
    
    # Crear atributos de producto (ProductAttribute)
    side_effects = ProductAttribute.objects.create(
        name="Side Effects",
        product=product1,
        values=["hives", "difficulty breathing", "swelling of your face"]
    )
    # side_effects.values.set(["hives", "difficulty breathing", "swelling of your face"])
    
    pregnancy_category = ProductAttribute.objects.create(
        name="Pregnancy Category",
        product=product1,
        values=["C"]
    )
    # pregnancy_category.values.set(["C"])
    
    rx_otc = ProductAttribute.objects.create(
        name="Rx/OTC",
        product=product1,
        values=["Rx"]
    )
    # rx_otc.values.set(["Rx"])
    
    # Crear variaciones de producto (ProductVariation)
    variation1 = ProductVariation.objects.create(
        # id="var2",
        sku=get_object_or_404(Product, pk="6676e6fad91161434cdd4f69"),
        image="https://emhvpljjyqwgxxtsiylw.supabase.co/storage/v1/object/public/public/sw2_crm/products/Benzaclin_1.jpeg",
        description="Benzaclin 50mg",
        price=20.99,
        sale_price=18.99,
        stock=75,
        # product=product1,
        attribute_values={"Dosage": "50mg"},
        branch=branch1
    )
    # variation1.attribute_values = {"Dosage": "50mg"}
    variation1.save()
    
    variation2 = ProductVariation.objects.create(
        # id="2",
        sku=get_object_or_404(Product, pk="6676e6fad91161434cdd4"),
        image="https://emhvpljjyqwgxxtsiylw.supabase.co/storage/v1/object/public/public/sw2_crm/products/Tetracycline_4.jpg",
        description="Tetracycline 250mg",
        price=30.99,
        sale_price=28.99,
        stock=100,
        # product=product2,
        attribute_values = {"Dosage": "250mg"},
        branch=branch1
    )
    # variation2.attribute_values = {"Dosage": "250mg"}
    variation2.save()

    # Crear movimientos de inventario (InventoryMovement)
    movement1 = InventoryMovement.objects.create(
        product=product1,
        quantity=50,
        movement_type="IN",
        modified_by= get_object_or_404(Personal, pk=1),
        branch=branch1
    )
    
    movement2 = InventoryMovement.objects.create(
        product=product2,
        quantity=-25,
        movement_type="OUT",
        modified_by= get_object_or_404(Personal, pk=1),
        branch=branch1
    )

    print("Datos poblados exitosamente.")

# Llamar a la función para poblar datos
populate_data()
