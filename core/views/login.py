from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    '''
    TemplateView usado para nuestro home.
    
    **Template:**
    
    :template:`core`
    '''
    template_root = "core/auth/"
    template_name= template_root + "login.html"
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('core:home') 
