from django.http import HttpResponse
from django.shortcuts import render

# View para a página inicial
def home(request):
    return render(request, 'home.html')  
