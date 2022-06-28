from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Address
from .forms import AddressForm

# Create your views here.



def listar(request):
    address = Address.objects.all()

    context ={
        'address': address
    }

    return render(request, "listar.html", context)

def cadastrar(request):


    form = AddressForm(request.POST or None)
    
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        print('foi')
        return redirect('url_listar')

    context ={
        'form': form
    }

    return render(request, 'cadastrar.html', context)