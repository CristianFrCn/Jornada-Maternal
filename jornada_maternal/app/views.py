from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente

def site(request):
    return render(request, 'site.html')
def redefenir(request):
    return render(request, 'redefenir.html')
def cadastro(request):
    return render(request, 'cadastro.html')
def login(request):
    return render(request, 'loginusuario.html')
def vacina(request):
    return render(request, 'abaVacina.html')
def prenatal(request):
    return render(request, 'abaPreNatal.html')
def mais(request):
    return render(request, 'abaMais.html')
def amamentacao(request):
    return render(request, 'subAmamentacao.html')
def noticias(request):
    return render(request, 'subNoticias.html')
def chat(request):
    return render(request, 'subChat.html')


def cep(request):
    return render(request, 'cep.html')

def create_cliente(request):
    cliente_form = ClienteForm(request.POST or None, request.FILES or None)
    if(cliente_form.is_valid()):
        cliente = cliente_form.save(commit=False)
        cliente.save()
        return redirect("read_cliente")
    return render(request, 'create_cliente.html', {'cliente_form':cliente_form})

def read_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_read.html', {'clientes':clientes})

def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente_form = ClienteForm(request.POST or None,
                               request.FILES or None,
                               instance=cliente)
    if(cliente_form.is_valid()):
        cliente = cliente_form.save(commit=False)
        cliente.save()
        return redirect("read_cliente")
    return render(request, 'create_cliente.html', {'cliente_form':cliente_form})

def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect("read_cliente")