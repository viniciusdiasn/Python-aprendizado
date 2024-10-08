# -*- coding: utf-8 -*-
"""18 de maio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GRhcHDrqh8W2bqpY399U2pEbN0otMNBH

# FUNÇOES EM PYTHON

Funções detro de funções
"""

# @title Exemplo de função dentro de função

def soma(lst):
    total=0
    for e in lst:
        total+=e
    return total

def media(lista):
    resultado=soma(lista)/len(lista)    # Resultado tera a media a media da lista
    return resultado

lista= [4,7,15,28,54]
media(lista)

"""Outro exemplo de função dentro de uma função"""

# @title  Exemplo de funçao - épar

def ehpar(n):   # assinatura da função
    return n%2 == 0 # retorno da função: sera true para par  e flase para impar

ehpar(8)
ehpar(15)

# @title Exemplo de função de par ou imapr

def par_ou_impar(p):
    if ehpar(p):
       return "é par "
    else:
        return 'é impar'



par_ou_impar(27)

"""# ESCOPO E TEMPO DE VIDA DAS VARIAVEIS"""

# @title escopo e tempo de vida exemplos

def teste():
    xis = 300
    print(f'Na função teste o meu numero xis vale {xis}\n')
    print(f'Na função teste numero vale {numero}')

teste()

#progama principal

numero=97


print(f'No progama principal numero vale {numero}')

print(f'No progama principal xis vale {xis}')

"""# Ajuda interativa - Interective Help"""

help()

"""# documentação da função - doc strings

docstrings são a forma de adicionar como ou o que faz para um usuario

Eles são acessados atraves do comando help(nome_da_função)

use 3 aspas duplas (2x) logo depois da definição da função



```
# Isto está formatado como código
def nomedafuncao(nomedoparametro)
      '''
    -> Essa funcao faz tal coisa...
    :param: nomedoparametro: usado para etc...
    :param: ......
    :param: ...

    corpo da função vem aqui


```


"""

# @title uma função com docstring

def exemplodoc(nome , data):
    """
    -> Essa função mostra como criar um
    - minihelp da função
    :param nome: de exemplo
    :param datta: de exemplo
    """
    print(f'O nome desconhecido foi {nome} e a data foi {data}\n')

exemplodoc('Carlos', '18/05/2024')

help(exemplodoc)

"""# Modulos em python

Vamos importar o modulo de funçoes matematicas - math

e verificar quais funçoes ele tem.

use o comando dor(nome_do_modulo)
"""

import math

# esse jeito de importar traz Todas as funçoes em math

dir(math)   # Para ver todas as funçoes existentes no modulo math

len(dir(math))

# @title Exemplo de importação seletiva em um modulo

#from random import random #importar do modulo random a função random

from random import random as aleatorio

for i in range(5):
    print(aleatorio())

# @title Outtro exemplo de importação seletiva em um modulo

 from platform import platform
 from platform import machine


 print(platform())
 print(machine())