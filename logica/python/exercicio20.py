# Crie uma função em Python chamada 'listas_sao_iguais' que receba
# duas listas como argumentos.
#
# A função deve retornar `True` se as duas listas contiverem **exatamente os mesmos elementos**,
# independentemente da ordem. Retorne `False` caso contrário.
#
# **Regras:**
# - As listas podem ter tamanhos diferentes se houver duplicatas.
# - Não use a conversão direta para `set()` para comparar. Pense em contar ocorrências ou ordenar.


def listas_sao_iguais(lista1, lista2):
    return sorted(lista1) == sorted(lista2)
  
            
            
lista1_usuario = ['1', '2', '3', '4', 'vaca']
lista2_usuario = ['1', '2', '3', '4', 'vaca', 'boi']
resultado = listas_sao_iguais(lista1_usuario, lista2_usuario)
print(resultado)