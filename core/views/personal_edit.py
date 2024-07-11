from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Personal, Rol
from django.utils import timezone
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class PersonalEditView(LoginRequiredMixin, generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/personal/"
    template_name= template_root + "personal.edit.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personal_id = kwargs.get('personal_id')
        personal = get_object_or_404(Personal, pk=personal_id)
        roles = Rol.objects.all()
        context['data'] = {
            'personal': personal,
            'roles': roles,
        }
        return context
    
    def post(self, request, *args, **kwargs):
        personal_id = kwargs.get('personal_id')
        personal = get_object_or_404(Personal, pk=personal_id)

        personal.nombres = request.POST.get('nombres')
        personal.apellidos = request.POST.get('apellidos')
        
        fecha_nacimiento_str = request.POST.get('fecha_nacimiento')
        fecha_nacimiento_str = fecha_nacimiento_str.split('T')[0]  # Elimina todo después de 'T'


        
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()

        personal.fecha_nacimiento = fecha_nacimiento
        personal.telefono = request.POST.get('telefono')
        personal.email = request.POST.get('email')
        personal.estado = request.POST.get('estado')
        personal.fecha_inicio = request.POST.get('fecha_inicio')
        personal.salario = request.POST.get('salario')
        
        rol_id = request.POST.get('cargo_id')
        rol = get_object_or_404(Rol, pk=rol_id)
        personal.rol = rol

        personal.save()

        return redirect('core:personal')

