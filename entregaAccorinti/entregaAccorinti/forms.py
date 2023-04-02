from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion']

class BuscarLibroForm(forms.Form):
    titulo = forms.CharField(max_length=100)

    def buscar(self):
        titulo = self.cleaned_data['titulo']
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return libros