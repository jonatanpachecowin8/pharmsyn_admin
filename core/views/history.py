from django.views import generic
from core.models.ventas.order import Order
from django.contrib.auth.mixins import LoginRequiredMixin

class HistoryView(LoginRequiredMixin, generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/historial/"
    template_name= template_root + "history.list.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        orders = Order.objects.all()[:10]
       
        context['orders'] = orders
        return self.render_to_response(context)

