from DataExport.FacturacionForm import FacturacionForm
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Facturacion
import csv
from django.http import HttpResponse

def reset_datos(request):
    Facturacion.objects.all().delete()
    return render (request, 'home.html')

def respuesta(request):
    facturas = Facturacion.objects.all()
    return render(request, 'respuesta.html', {'facturas': facturas})

def home(request):
    if request.method == "POST":
        form = FacturacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('respuesta')
    else:
        form = FacturacionForm()
    return render(request, 'home.html', {'form': form})

def reset_datos(request):
    Facturacion.objects.all().delete()
    return redirect('home')

def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="facturas.csv"' # TODO: añadir timestamp en nombre de archivo

    writer = csv.writer(response)
    writer.writerow(['Nombre Cliente', 'Dirección', 'Producto', 'Cantidad', 'Precio Total', 'Fecha'])

    facturas = Facturacion.objects.all().values_list('nombre_cliente', 'direccion', 'producto', 'cantidad', 'precio_total', 'fecha')
    for factura in facturas:
        writer.writerow(factura)

    return response