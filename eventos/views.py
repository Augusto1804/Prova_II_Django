from django.shortcuts import render, redirect
from .forms import EventoForm

eventos_lista = []

def menu(request):
    return render(request, 'menu.html', {'eventos': eventos_lista})

def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)

        if form.is_valid():
            evento = form.cleaned_data['evento']
            local = form.cleaned_data['local']

            eventos_lista.append({
                'evento': evento,
                'local': local
            })

            return redirect('menu')
    else:
        form = EventoForm()

    return render(request, 'novo.html', {'form': form})
