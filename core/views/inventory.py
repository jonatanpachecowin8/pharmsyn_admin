from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import InventoryMovement
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class InventoryView(LoginRequiredMixin, generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/inventory/"
    template_name= template_root + "inventory.list.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inventory_list = InventoryMovement.objects.all()

        context['inventories'] = inventory_list
        return context