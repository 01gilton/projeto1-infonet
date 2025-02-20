from django.urls import path
from .views import listar, cadastrar, editar, excluir

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('editar/<int:produto_id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
]
