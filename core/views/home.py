from django.views import generic
from django.shortcuts import render
from core.models.cliente.user import User
from core.models.ventas.order import Order
from core.models.product.product import Product
from django.db.models import Sum
import json
from django.db.models.functions import TruncDate

class HomeView(generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/"
    template_name= template_root + "home.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Obtener datos desde la base de datos
        new_users_count = User.objects.filter(date_joined__gte='2024-01-01').count()  # Ajusta la fecha según tu necesidad
        new_orders_count = Order.objects.filter(order_date__gte='2024-01-01').count()  # Ajusta la fecha según tu necesidad
        total_sales_amount = Order.objects.filter(order_date__gte='2024-01-01').aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0

        
        orders = Order.objects.all()
        product_count = {}

        # Iterar sobre cada pedido y actualizar la sumatoria de productos
        for order in orders:
            items = order.items  # Obtener los items del pedido como lista de diccionarios
            for item in items:
                product_id = item['product_id']
                quantity = item['quantity']

                # Actualizar la sumatoria de productos por product_id
                if product_id in product_count:
                    product_count[product_id]['total_quantity'] += quantity
                else:
                    product_count[product_id] = {
                        'total_quantity': quantity,
                        'product_id': product_id,
                        'product_name': None  # Inicialmente estableceremos el nombre como None
                    }

        # Obtener los nombres de los productos basados en los product_ids únicos
        product_ids = list(product_count.keys())

        # Consultar los nombres de los productos desde la base de datos
        products = Product.objects.filter(id__in=product_ids).values('id', 'title')

        # Mapear los nombres de los productos a product_count
        product_names = {product['id']: product['title'] for product in products}

        # Asignar los nombres de los productos a product_count
        for product_id, data in product_count.items():
            data['product_name'] = product_names.get(product_id, 'Unknown Product')

        # Convertir a una lista de tuplas para ordenar por cantidad total
        top_products = [(data['product_name'], data['total_quantity']) for product_id, data in product_count.items()]

        # Ordenar los productos por cantidad descendente
        top_products.sort(key=lambda x: x[1], reverse=True)

        # Limitar a los 3 productos más comprados
        top_products = top_products[:3]

        top_products_formatted = [
        {"label": product_id, "value": total_quantity}
        for product_id, total_quantity in top_products
        ]



        year = 2024
        month = 7
        order_data_queryset = Order.objects.filter(
            order_date__year=year,
            order_date__month=month
        ).annotate(
            date=TruncDate('order_date')  # Trunca a la fecha (sin la parte de tiempo)
        ).values(
            'date', 'branch_id'
        ).annotate(
            total_amount=Sum('total_amount')  # Suma del campo total_amount
        ).order_by(
            'date'
        )        
        # print(order_data_queryset)
        stacked_data = self.process_order_data(order_data_queryset)
        print(stacked_data)

        # Agregar datos al contexto
        context['new_users_count'] = new_users_count
        context['new_orders_count'] = new_orders_count
        context['total_sales_amount'] = total_sales_amount
        context['top_products'] = top_products
        context['top_products_j'] = json.dumps(top_products_formatted)
        
        return self.render_to_response(context)


    def process_order_data(self,order_data_queryset):
        stacked_data = []
        print(order_data_queryset)

        for order in order_data_queryset:
            date = order['date']  # Acceder a la fecha desde el diccionario
            print(date)
            branch_id = order['branch_id']  # Acceder al branch_id desde el diccionario
            total_amount = order['total_amount']  # Acceder al total_amount desde el diccionario
                
                # Verificar si la fecha ya existe en stacked_data
            existing_entry = next((entry for entry in stacked_data if entry['date'] == date), None)
                
            if existing_entry:
                # Si la fecha ya existe, actualizar el total_amount correspondiente al branch_id
                existing_entry[branch_id] = total_amount
            else:
                # Si la fecha no existe, crear una nueva entrada
                new_entry = {'date': date, 'branch_id': branch_id, branch_id: total_amount}
                stacked_data.append(new_entry)
        

        return stacked_data