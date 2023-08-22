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

def cep(request):
    return render(request, 'cep.html')

def create_Gestante(request):
        Gestante_form =   GestanteForm(request.POST or None, request.FILES or None)
        if (Gestante_form.is_valid()):
            Gestante =   Gestante_form.save(commit=False)
            Gestante.save()
            return redirect("read_Gestante")
        return render(request, 'create_Gestante.html', {'Gestante_form': Gestante_form})

    def read_Gestante(request):
        Gestante = Gestante.objects.all()
        return render(request, 'Gestante_read.html', {'Gestante': Gestante})

    def update_Gestante(request, id):
        Gestante = get_object_or_404(Gestante, pk=id)
        Gestante_form = GestanteForm(request.POST or None,
                                   request.FILES or None,
                                   instance=Gestante)
        if (Gestante_form.is_valid()):
            Gestante = Gestante_form.save(commit=False)
            Gestante.save()
            return redirect("read_Gestante")
        return render(request, 'create_Gestante.html', {'Gestante_form': Gestante_form})

    def delete_Gestante(request, id):
        Gestante = get_object_or_404(Gestante, pk=id)
        Gestante.delete()
        return redirect("read_Gestante")
