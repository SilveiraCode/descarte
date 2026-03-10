import json
from django.shortcuts import render, redirect
from .models import PontoColeta,  SolicitacaoColeta
from .forms import  SolicitacaoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

def dashboard(request):
    pontos_db = PontoColeta.objects.all()
    dados_mapa = [
        {'nome': p.nome, 'lat': p.latitude, 'lng': p.longitude, 'info': p.get_tipo_residuo_display()}
        for p in pontos_db
    ]
    return render(request, 'index.html', {'pontos_json': json.dumps(dados_mapa)})

def nova_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid():
            # 1. Cria o objeto, mas não salva no banco ainda (commit=False)
            solicitacao = form.save(commit=False)
            
            # 2. Atribui o usuário logado ao campo 'usuario' do modelo
            solicitacao.usuario = request.user 
            
            # 3. Agora sim, salva no banco de dados com o ID do usuário
            solicitacao.save()
            
            return redirect('lista_solicitacoes')
    else:
        form = SolicitacaoForm()
    
    return render(request, 'solicitar.html', {'form': form})
def lista_solicitacoes(request):
    solicitacoes = SolicitacaoColeta.objects.all().order_by('-id')
    return render(request, 'lista_solicitacoes.html', {'solicitacoes': solicitacoes})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            # Se o ADMIN está cadastrando, volta para a lista. Se não, vai para o login.
            if request.user.is_superuser:
                return redirect('lista_usuarios')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def lista_usuarios(request):
    usuarios = User.objects.all().order_by('-date_joined')
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})
