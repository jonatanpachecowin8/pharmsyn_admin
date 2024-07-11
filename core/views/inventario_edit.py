from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Product, InventoryMovement, Branch
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class InventarioEditView(LoginRequiredMixin, generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/inventory/"
    template_name= template_root + "inventory.edit.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inventory_id = kwargs.get('inventory_id')
        inventory = get_object_or_404(InventoryMovement, pk=inventory_id)
        branchs = Branch.objects.all()
        products = Product.objects.all()
        context['data'] = {
            'products': products,
            'branchs': branchs,
            'inventory': inventory,
        }
        return context
    
#     def post(self, request, *args, **kwargs):
#         inventory_id = kwargs.get('inventory_id')
#         inventory = get_object_or_404(InventoryMovement, pk=inventory_id)

#         product.stock = request.POST.get('stock')
#         product.price = request.POST.get('price')
#         product.sale_price = request.POST.get('sale_price')
        
#         # product.sale_price = fecha_nacimiento
#         product.title = request.POST.get('title')
#         # product.thumbnail = request.POST.get('email')
#         # product.product_type = request.POST.get('product_type')

#         laboratory_id = request.POST.get('laboratory_id')
#         laboratory = get_object_or_404(Laboratory, pk=laboratory_id)

#         product.laboratory = laboratory

#         product.description = request.POST.get('description')

#         category_id = request.POST.get('category_id')
#         category = get_object_or_404(Category, pk=category_id)
#         product.category = category
# # 
#         product.save()

#         return redirect('core:product')

