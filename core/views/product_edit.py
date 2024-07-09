from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Product, Category, Laboratory
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import datetime


class ProductEditView(generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/drug/"
    template_name= template_root + "drug.edit.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        labortories = Laboratory.objects.all()
        categories = Category.objects.all()
        context['data'] = {
            'product': product,
            'laboratories': labortories,
            'categories': categories,
        }
        return context
    
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        product.stock = request.POST.get('stock')
        product.price = request.POST.get('price')
        product.sale_price = request.POST.get('sale_price')
        
        # product.sale_price = fecha_nacimiento
        product.title = request.POST.get('title')
        # product.thumbnail = request.POST.get('email')
        # product.product_type = request.POST.get('product_type')

        laboratory_id = request.POST.get('laboratory_id')
        laboratory = get_object_or_404(Laboratory, pk=laboratory_id)

        product.laboratory = laboratory

        product.description = request.POST.get('description')

        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        product.category = category
# 
        product.save()

        return redirect('core:product')

