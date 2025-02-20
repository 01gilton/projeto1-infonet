from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["descricao", "preco"]
        widgets = {
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Descrição"}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "placeholder": "Preço"}),
        }