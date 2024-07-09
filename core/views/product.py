from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Product
from django.utils import timezone
from django.urls import reverse_lazy


class ProductView(generic.TemplateView):
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

        context['products'] = product_list
        return context