from django.shortcuts import render
from .forms import LibroForm

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

def buscar_libro(request):
    if request.method == 'POST':
        form = BuscarLibroForm(request.POST)
        if form.is_valid():
            libros = form.buscar()
            return render(request, 'resultado_busqueda.html', {'libros': libros})
    else:
        form = BuscarLibroForm()
    return render(request, 'buscar_libro.html', {'form': form})