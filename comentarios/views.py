from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from .forms import ComentarioForm

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'comentarios/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    comentarios = articulo.comentarios.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.save()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/detalle_articulo.html', {'articulo': articulo, 'comentarios': comentarios, 'form': form})
