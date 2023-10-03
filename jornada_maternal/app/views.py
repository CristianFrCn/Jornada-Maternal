from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .utils import google_custom_search
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth import views
from django.shortcuts import render, redirect
from django.contrib import messages



def site(request):
    return render(request, 'site.html')
def redefenir(request):
    return render(request, 'password_reset_complete.html')




def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('index')

        else:
            print('invalid registration details')

    return render(request, "registration/register.html", {"form": form})

def login(request):
    return render(request, 'loginusuario.html')

@login_required
def vacina(request):
    return render(request, 'abaVacina.html')

@login_required
def prenatal(request):
    return render(request, 'abaPreNatal.html')
def mais(request):
    return render(request, 'abaMais.html')
def amamentacao(request):
    return render(request, 'subAmamentacao.html')
def noticias(request):
    return render(request, 'subNoticias.html')


@login_required
def chat(request):
    return render(request, 'subChat.html')
def informacoes(request):
    return render(request, 'adicionarinformacoes.html')
def menu(request):
    return render(request, 'cliente_read.html')

def cep(request):
    return render(request, 'cep.html')

def search_results(request):
    query = request.GET.get('q')
    if query:
        results = google_custom_search(query)
    else:
        results = []

    context = {'results': results, 'query': query}
    return render(request, 'search_results.html', context)

@login_required
def create_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, request.FILES)
        if cliente_form.is_valid():
            cliente = cliente_form.save(commit=False)
            cliente.save()
            return redirect("read_cliente")
    else:
        cliente_form = ClienteForm()

    return render(request, 'cliente_create.html', {'cliente_form': cliente_form})


@login_required
def read_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_read.html', {'clientes':clientes})

@login_required
def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente_form = ClienteForm(request.POST or None,
                               request.FILES or None,
                               instance=cliente)
    if(cliente_form.is_valid()):
        cliente = cliente_form.save(commit=False)
        cliente.save()
        return redirect("read_cliente")
    return render(request, 'cliente_create.html', {'cliente_form':cliente_form})
@login_required
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect("read_cliente")

