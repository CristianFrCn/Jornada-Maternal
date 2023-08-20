from django.shortcuts import render, redirect, get_object_or_404
from .forms import GestanteForm
from .models import Gestante

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

    def create_adicional(request):
        Gestante_form =   GestanteForm(request.POST or None, request.FILES or None)
        if (Gestante_form.is_valid()):
            Gestante =   Gestante_form.save(commit=False)
            Gestante.save()
            return redirect("read_adicional")
        return render(request, 'create_adicional.html', {'cliente_form': cliente_form})

    def read_adicional(request):
        Gestante = Gestante.objects.all()
        return render(request, 'gestante_read.html', {'clientes': clientes})

    def update_adicional(request, id):
        Gestante = get_object_or_404(Gestante, pk=id)
        Gestante_form = GestanteForm(request.POST or None,
                                   request.FILES or None,
                                   instance=Gestante)
        if (Gestante_form.is_valid()):
            Gestante = Gestante_form.save(commit=False)
            Gestante.save()
            return redirect("read_cliente")
        return render(request, 'create_adicional.html', {'cliente_form': cliente_form})

    def delete_adicional(request, id):
        Gestante = get_object_or_404(Gestante, pk=id)
        Gestante.delete()
        return redirect("read_Gestante")
