from django.shortcuts import render
from passagens.forms import PassagemForms, Pessoaform

def index(request):
    form = PassagemForms()
    pessoa_form = Pessoaform()
    contexto = {'form':form,
                 'pessoa_form': pessoa_form}
    return render(request, 'index.html', contexto)

def minha_passagem(request):
    form = PassagemForms(request.POST)
    pessoa_form = Pessoaform(request.POST)
    contexto = {'form':form,
                 'pessoa_form': pessoa_form}


    if form.is_valid():
        return render(request, 'minha_passagem.html', contexto)
    else:
        print('invalido ok')
        return render(request, 'index.html', contexto)     