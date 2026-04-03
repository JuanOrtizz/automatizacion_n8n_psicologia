from django.http import JsonResponse
from django.shortcuts import render
from .forms import SesionesForm

def dashboard(request):
    return render(request, 'dashboard/index.html')

def registrar_sesion(request):
    if request.method == 'POST':
        form = SesionesForm(request.POST)
    else:
        form = SesionesForm()
    return render(request, 'dashboard/register_sesion.html', {'form': form})