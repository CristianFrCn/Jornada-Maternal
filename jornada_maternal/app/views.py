from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def redefenir(request):
    return render(request, 'redefenir.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def inicio(request):
    return render(request, 'inicio.html')

def abaVacina(request):
    return render(request, 'abaVacina.html')

def abaPreNatal(request):
    return render(request, 'abaPreNatal.html')

def abaMais(request):
    return render(request, 'abaMais.html')

def subAmamentacao(request):
    return render(request, 'abaMais.html')

def subNoticias(request):
    return render(request, 'subNoticias.html')

def subChat(request):
    return render(request, 'subChat.html')


