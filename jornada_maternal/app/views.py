from django.shortcuts import render


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
