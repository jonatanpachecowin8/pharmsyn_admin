from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Product, Laboratory, Category
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductView(LoginRequiredMixin, generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/drug/"
    template_name= template_root + "drug.list.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_list = Product.objects.all()

        labortories = Laboratory.objects.all()
        categories = Category.objects.all()
        context['products'] = product_list
        context['laboratories'] = labortories
        context['categories'] = categories
        
        return context
    

    def add_product(self, request, *args, **kwargs):
        # Obtener los datos del formulario
        title = request.POST.get('title')
        stock = request.POST.get('stock')


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
        
        # Crear un nuevo objeto Product
        product = Product.objects.create(title=title, stock=stock)

        return redirect('core:product')