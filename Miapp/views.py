# items/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'items/item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {
        'form': form,
        'form_mode': 'crear'
    })

def item_update(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_form.html', {
        'form': form,
        'form_mode': 'editar'  # Indica que es el modo de edición
    })

def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})

def item_confirm_delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})