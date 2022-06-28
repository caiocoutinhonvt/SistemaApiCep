from django.forms import ModelForm
from .models import Address
from django import forms



class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'endereco', 'bairro', 'cidade', 'complemento', 'descricao', 'uf', 'numero']

        widgets = {

            'cep' :forms.TextInput(attrs={'id':'cep','class':'form-control cep','placeholder':'Digite seu CEP',
             'onblur':"pesquisacep(this.value);"}),
            'endereco': forms.TextInput(attrs={'id':'endereco','class':'form-control'}),
            'bairro': forms.TextInput(attrs={'id':'bairro', 'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'id':'cidade','class':'form-control'}),
            'complemento': forms.TextInput(attrs={'id': 'complemento','class':'form-control'}),
            'descricao': forms.TextInput(attrs={'id': 'descricao', 'class':'form-control'}),
            'uf': forms.TextInput(attrs={'id': 'uf', 'class':'form-control'}),
            'numero': forms.NumberInput(attrs={'id': 'numero', 'class':'form-control', 'type':'number'}),
        }