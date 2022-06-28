from rest_framework import viewsets
from myapp.api import serializers
from myapp import models
from django.http import JsonResponse
from myapp.models import Address
from .serializers import AddressSerializer
import requests



def check_cep(request,cep):

    address_from_database = Address.objects.filter(cep=cep).first()
    if address_from_database:
        data = AddressSerializer(address_from_database).data
        del data['id']
        return JsonResponse(data, safe=False)

    else:
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        
        if r.status_code == 200:
            address_from_viacep = r.json()

            data = {
                "cep": cep, 
                "endereco": address_from_viacep['logradouro'],
                "bairro": address_from_viacep['bairro'],
                "cidade": address_from_viacep['localidade'], 
                "uf": address_from_viacep['uf'], 
            }
        return JsonResponse(data, safe=False)
