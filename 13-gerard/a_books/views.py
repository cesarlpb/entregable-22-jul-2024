from django.shortcuts import render
from django.http import JsonResponse
from .forms import FiltrarLibrosForm
from .models import Saga, Libro, Autor

def sagas(request, autor_id):
    sagas = Saga.objects.filter(autor__id=autor_id)
    data = {'sagas': list(sagas.values('id', 'nombre'))}
    return JsonResponse(data)

def libros(request):
    saga_id = request.GET.get('saga_id')
    libros = Libro.objects.filter(saga_id=saga_id).order_by('titulo')
    return render(request, 'books/libro_list.html', {'libros': libros})

def busqueda_libros(request):
    form = FiltrarLibrosForm
    libros = Libro.objects.all()
    return render(request, 'books/search_books.html', {'form': form, 'libros': libros})
