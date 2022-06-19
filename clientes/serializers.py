from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        # criar uma validação direto no serializers //self é a instância
        # a partir de data vamos buscar os campos
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de cpf inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve ter apenas letras"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O rg deve ter 9 digitos'}) 
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O numero de celular deve seguir este modelo: 11 91234-1234, respeitando os espaço e traço.'})       
        return data
      
        
              
  
      
      
      
    """ metodo inicial  
    def validate_cpf(self, cpf):
      if len(cpf!=11):
        raise serializers.ValidationError('O cpf deve ter 11 digitos')
      return cpf
      # criar a função para validar o nome
    def validate_nome(self, nome):
      if not nome.isalpha():
        raise serializers.ValidationError('O nome deve ter apenas letras')
      return nome
    def validate_rg(self, rg):
      if len(rg)!=9:
        raise serializers.ValidationError('O rg deve ter 9 digitos')
      return rg
    def validate_celular(self, celular):
      if len(celular) < 11:
        raise serializers.ValidationError('O celular deve 11 digitos')
      return celular
     """
      
    