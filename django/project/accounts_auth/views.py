from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

class SignUpView(CreateView):
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')
