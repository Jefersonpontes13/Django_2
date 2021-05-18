from django.shortcuts import render


def index(request):
    return render(request, 'index.html', template_name='index')


def contato(request):
    return render(request, 'contato.html', template_name='contato')


def produto(request):
    return render(request, 'produto.html', template_name='produto')
