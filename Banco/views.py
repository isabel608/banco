from django.shortcuts import render, redirect
from .forms import ClienteForm, CuentaForm, TransaccionForm


def registrar_cliente(request):

    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('registrar_clientes')

    return render(request, 'registro_clientes.html', {'form': form})


def registrar_cuenta(request):

    form = CuentaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('registrar_cuentas')

    return render(request, 'registro_cuentas.html', {'form': form})


def registrar_transaccion(request):

    form = TransaccionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('registrar_transaccion')

    return render(request, 'registro_transaccion.html', {'form': form})

def consultas(request):
    listado_clientes= consultas.objects.all()
    
    return render(request, 'consultas.html',{'clientes':listado_clientes})

def registro(request):
    return render(request,'registro.html')

def visualizar(request,cliente_dpi):
    
    cuentas= Cliente.objects.filter(cliente = cliente_dpi)
    return render(request, 'registro.html',{'cuentas': cuentas})

def transferencia(request,numero_cuenta):
    if request.method=="POST":
        transaccion = TransaccionForm(request.POST)
        if transaccion.is_valid():
            info = transaccion.cleaned_data
            return render(request, 'formato.html')
    else:
        transaccion = TransaccionForm()
        
        return render(request,'transferencia.html',{'transaccion_form':transaccion,'numero_cuenta':numero_cuenta})
    
def guardartransa(request,numero_cuenta):
    
    if request.method=="POST":
        transaccion = TransaccionForm(request.POST)
        if transaccion.is_valid():
            info= transaccion.cleaned_data
            
            cuenta1 = cuenta.objects.get(numero_cuenta=info["cuenta"])
            cuenta2 = cuenta.objects.get(numero_cuenta=numero_cuenta)
            
            c_deposito = Transaccion.objects.create(
                cuenta = cuenta1,
                tipo = 'deposito',
                monto = info["monto"],
                descripcion = info["descripcion"]
            )
            
            c_retiro = Transaccion.objects.create(
                cuenta = cuenta2,
                tipo ='retiro',
                monto = info["monto"],
                descripcion = info["descripcion"]
            )
            
            cuenta1.saldo+=Decimal(info["monto"])
            cuenta1.save()
            
            cuenta2.saldo-=Decimal(info["monto"])
            cuenta2.save()
            
            return redirect('vsualizar',cuenta1.cliente.dpi)
        else:
            return HttpResponse("Datos invalidos, porfavor revisa el formulario.")