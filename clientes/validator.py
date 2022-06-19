import re
from validate_docbr import CPF

def nome_valido(nome):
  return nome.isalpha()

def cpf_valido(numero_cpf):
    cpf = CPF()    
    return cpf.validate(numero_cpf)  

def rg_valido(rg):
  return len(rg) == 9
        
def celular_valido(celular):
  return len(celular) == 11
        
def celular_valido(numero_celular):
  '''Verifica se o celurar é válido'''
  modelo = '[0-9]{2}\ ?[0-9]{5}-[0-9]{4}'
  resposta = re.findall(modelo, numero_celular)
  return resposta
      
  
  
     
  