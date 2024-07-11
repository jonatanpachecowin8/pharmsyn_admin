from django.views import generic
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Personal
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PersonalView(LoginRequiredMixin, generic.TemplateView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/personal/"
    template_name= template_root + "personal.list.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personal_list = Personal.objects.select_related('rol').all()

        today = timezone.now().date()
        processed_personal = []
        for person in personal_list:
            age = today.year - person.fecha_nacimiento.year - (
                (today.month, today.day) < (person.fecha_nacimiento.month, person.fecha_nacimiento.day)
            )
            processed_personal.append({
                'id': person.id,
                'nombres': person.nombres,
                'apellidos': person.apellidos,
                'edad': age,
                'telefono': person.telefono,
                'email': person.email,
                'estado': person.estado,
                'fecha_inicio': person.fecha_inicio,
                'salario': person.salario,
                'rol': person.rol
            })
        
        context['personal'] = processed_personal
        return context