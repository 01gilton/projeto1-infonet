from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'produtos/pages/listar.html')


