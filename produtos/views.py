from django.shortcuts import render, redirect, get_object_or_404# importar o redirect
from .models import Produto
from .forms import ProdutoForm # Importação da classe ProdutoForm


def listar(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/pages/listar.html", {"produtos": produtos})

# Criação da View cadastrar()
def cadastrar(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = ProdutoForm()
    
    return render(request, "produtos/pages/cadastrar.html", {"form": form})

def editar(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, "produtos/pages/editar.html", {"form": form})

def excluir(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("listar")  # Redireciona para a lista de produtos após a exclusão