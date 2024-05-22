
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import medForm
from .models import medList

from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def product_create(request):
    if request.method == 'POST':
        form = medForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form = medForm()
    return render(request, 'create.html', {'form': form})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required(login_url='/login/')
def product_read(request):
    medicine_list = medList.objects.all()
    search_term = request.GET.get('search')
    if search_term:
        medicine_list = medicine_list.filter(Name__istartswith=search_term)
    return render(request,'retrieve.html',{'medicine_list':medicine_list})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def product_update(request, pk):
    product = medList.objects.get(pk = pk)
    if request.method == 'POST':
        form = medForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =medForm(instance=product)           
    return render(request, 'update.html', {'form': form})

from django.shortcuts import render
def product_delete(request,pk):
    product = medList.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('retrieveproduct')
    
    return render(request,'retrieve.html',{'product':product})