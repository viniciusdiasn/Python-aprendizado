# -*- coding: utf-8 -*-
"""Aula27deAbril.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_mWmrBw1TOtLVkM1XHLn98S7NNcHqsYR

# Cadeia de caracteres

manipulação de Textos em Pyton
"""

exem= 'cadeia de caracteres'
print(len(exem)) # uso de LEN para contar caracteres

s# @title Descobrindo quantas letras há na palavra

jedi= 'luke skywalker'
letras= len(jedi)
print(letras)

primeiraletra = jedi[0]
print(primeiraletra)

ultimaletra= jedi[13]
print(ultimaletra)

nome= jedi[0:4] # Fatiar uma palavra

print(nome)

"""fatiar uma palavra é selecionar quais caracteres

serão escolhidos e usados

usa-se os colchetes [] e dentro os índices dos

elementos da palavra que queremos usar

"""

# Exemplo de fatiamento de uma palavra

nome= jedi[0:4] # Exemplo de índice

print(nome) # exibir somente a primeira palavra

# Exemplo de fatiamento com indice negativo

sobrenome = jedi[-9:-1]
print(sobrenome)

# Um outro fatiamento
comeco= jedi[-9:]
print(comeco)

"""# operadores relacionais

"""

# @title Exercicios com operadores relacionais

a = 1 # a recebe valor 1
b = 5 # b recebe o valor 5
c = 2 # c recebe o valor 2
d = 1 # d recebe o valor 1


# Teste de iguadade

a == b # a é igual a b

b > a # b é maior  doque a?

b >= a # b é maior ou igual doque a?

c <= d # c é menor ou igual doque d?

# teste de desigualdade

d!= a # d é diferente de a ?

d != b # d é diferente de b?

# @title operadores de relacionais e variaveis

nota = 8 # valor da nota

media = 7

aprovado= nota > media # Criterio de aprovaçao

print(aprovado) # resultado do teste

# Exemplo de codigo com operadores logicos

num1= 7
num2= 4

num1 > 3 and num2 <8 # operação logica com and

# Exemplo de operaçao logica not

print('\nnot True =', not True)

print('\nnot False =', not False)

"""# Exercicio de aprovação de imprestimo

condição de aprovação de salario: salario> 1000 e idade 18
considerar salario igual a R$ 100,00 e idade igual a 20 anos
"""

# Exemplo de aprovação do imprestimo
# condição de aprovaçao: salario> 1000 e idade > 18

salario= 100
idade = 20

condicao= (salario>1000 and idade > 18)

print('O emprestimo foi aprovado?',condicao)

"""agora o slario e igual a R$ 2000 a e idade igual a 20."""

salario= 2000
idade = 20

condicao= (salario>1000 and idade > 18)

print('O emprestimo foi aprovado?',condicao)

"""# Formataçao a saida de texto"""

# Exemplo de formataçao de texto

 tutor = 'obiwan'

 print(tutor)
 print(jedi)

 print(f'O professor do {jedi} é o {tutor}')

# exemplo de formataçao de numero


x= 23
y= 49.76

z= x * y

print(f'o resultado de {x} * {y} é {x*y:.5f}')

"""# Estrutura de decisão"""

# Exemplo de condicional simples

idade= 17

if idade >= 18:
        print('voce é maior de idade')
print('voce é menor de idade')

# Exemplo de estrutura de decisão simples

age=19

print('hora do teste...\n')

# Exemplo de estrutura de decisão

tempo= int(input('quantos anos tem seu carro ?'))

if tempo <= 3:
   print('\nseu carro e novo')

if tempo >= 3:
   print('\nseu carro e velho')

resp= int(input('de 0 a 10 quanto o brenon e viado '))

if resp>=5:
    print('viadão')

if resp<=5:
   print('ele é bem mais gay')

# exemplo de estrutura de decisão composta

tempo=int(input('quantos anos vc tem'))
if tempo>50:
   print('ta bem veio')

else:
    print('ta novinho')

"""# exercicio 1

crie um progama que pede a idade do usuario

avalia de é maior ou igual a 18 anos

Exiba a mensagem " Maior de idade " ou " Menor de idade

"""

# Exercicio 1

idade=int(input(' digite sua idade lindão '))

if idade>=18:
   print('é maior de idade')
else:
    print('e de menor')

"""# Exercicio 2

Crie um progama que pede dus notas ao usuario e

calcula a media das notas

se a média for maior ou igual e 7 exiba a

mensagem"aluno aprovado" e a mensagm "Aluno reprovado"


"""

nota1=int(input('sua primeira nota '))
nota2=int(input('sua segunda nota '))

media= (nota1+nota2)/2

if media>7:
   print('voce foi aprovado com:', media)
else:
    print('voce foi reprovado com:', media)

# Exemplo de estrutura de desisão aninhada
print('\ntelefonica')

min=int(input('\nQuantos minutos voce gostaria '))

if min<200:
 preco=0.20
else:
  if min<400:
     preco=0.18
  else:
     preco= 0.15
print(f'\nVoce ira pagar este mes: R${min*preco:.2f}')

"""Exemplo de codigo com varias categorias"""

# Exemplo de código com varias categorias

print('inicio do progama...\n')

cat=int(input('qual a categoria do seu produto? '))
if cat== 1:
  pre= 10
else:
  if cat ==2:
    pre = 18
  else:
    if cat ==3:
      pre=23
    else:
      if cat == 4:
        pre=26
      else:
        if cat ==5:
          pre=31
        else:
          pre=0
          print('categoria invalida')

print(f'O preço do produto é R${pre:.2f}')

# Exemplo de código com varias categorias

print('inicio do progama...\n')

cat=int(input('qual a categoria do seu produto? '))
if cat ==1:
   pre =10
elif  cat==2:
    pre=18
elif  cat==3:
    pre=23
elif  cat==4:
    pre=26
elif  cat==5:
    pre=31
else:
    print('categoria invalida!')
    pre=0
print(f'o preço do produto éR${pre:.2f}')





print('categoria invalida')

print(f'O preço do produto é R${pre:.2f}')

"""# Exercicio 3

Crie um progama que pode 2 notas, calcule a media do aluno

se média maior ou igual a 7, exibe a mensagem aprovado,

se média maior ou igual que 5, exibe mensagem aprovado,

se media for menor que 5, exibe a mensagem de reprovado


"""

n1=int(input('digite a primeira nota \n'))
n2=int(input('digite a segunda nota \n'))
media=(n1+n2)/2
if  media>7:
    print('voce foi aprovado com media', media)
elif  media>5:
      print('voce foi aprovado com media', media)
elif  media<5:
      print('voce foi reprovado com media', media)

"""# exercicio 4
crie um progama que o usuario

coloque um numero que pode ser

negativo, postivo ou nulo
"""

num=float(input('digiti um numero '))
if  num>0:
    print('Seu numero é positivo')
elif  num<0:
      print(' seu numero é negativo')
elif  num>=0:
      print('seu numero é zero')

"""# Exercicio 5

crie uma variavel 'horario'

que diz se é a tarde, manha, noite e madrugada

"""

hora=int(input('Digite um horario '))
if  hora>=6 and hora<12:
    print('agora é de manha ')
elif  hora>=12 and hora<18:
      print('agora é de tarde')
elif  hora>=18 and hora<23:
      print('agora e noite')
elif  hora>=0  and hora<6:
      print('agora e de madrugada')

"""# Exercicio 6

Crie um progama que testa um numero inteiro

fornecido é par ou impar

# Estrutura de Repetição em Python
"""

# @title Um exemplo motivador

valor_total_compra = 0
valor_feijao= 5.5
valor_arroz= 4
valor_macarrao= 2

produto= input('\nDigite o codigo do produto ')

if  produto == 'feijao':
   # valor_total_compra=valor_total_compra+valor_feijao # Primeiro jeito

    valor_total_compra+=valor_feijao # jeito mais pratico
elif  produto== 'arroz':
          valor_total_compra+=valor_arroz

elif  produto== 'macarrao':
          valor_total_compra+=valor_macarrao

print(f'\nO valor da sua compra é R$ {valor_total_compra}')

"""# Entendendo o laço For"""

# Exemplo de repetição com for

for contador in range(10):
    print('monthy python!!')

# @title A indentificação

for n in range(10):
    print('no bloco')
    print('oi')
print('fora do bloco')

"""# Entendendo o laço for"""

for contagem in range(10):
    texto=str(contagem)
    print(f'o valor de contagem é {contagem}')

# Exemplo de interação com o for

frase= 'Ola senai'
for letra in frase:
    print(letra)

for c in range(0,100,10):
    print(c)

# Exemplo de laço for  e como é atualizado

print(' Inicio do progama de  repetição...\n')

texto = input('Qual a mensagem?')  # Solicita a mensagem e armazena na variavel
quantidade=int(input('Quantas vezes devo repitir? '))


for n in range(quantidade):
    mensagem= texto + '' + str(n) # Converte para texto e concatenada
    print(mensagem)

# Outro exemplo de interação pelo laço for
frase='Obiwan'
for letra in frase:
    print(letra)

# @title Exemplo de contador cresente

print('Inicio do contador ')

for z in range(50):
    print(z)

# @title exemplo de contador decresente

print('Inicio do contador ')

for n in range(100,-1,-1):
    print(n)

"""# Corrigindo o codigo do mercado"""

# O progama do mercado corrigido

print('\n Bem vindo ao nosso mercado ')

# Definir as variaveis
valortotal= 0
valorarroz= 4
valorfeijao= 2
valormacarrao= 2

for m in range(5):
    mercadoria= input(' Digite um produto ')

    if  mercadoria  ==  'feijao':
          valortotal+=valorfeijao
    elif  mercadoria== 'arroz':

        valortotal+=valorarroz
    elif mercadoria== 'macarrao':
        valortotal=+valortotal

print(f'\nSua compra deu R$ {valortotal} volte sempre ')

# @ title Entendendo o laço while

print(' Inicio do progama ')

controle = 1

while controle <10:# uso do laço while
      print(controle) # Emprima a variavel
      controle += 1 # Incrementa a variavel de uma unidade

print('\nFim do progama')

contador = 0

while contador < 10:
  if contador % 2 == 0:
    print(contador)
  contador+=1

# Um outro exemplo de laço while

contador  = 0

while contador  < 10:
      if  contador  % 2  ==  0:
          print(contador)
      contador  +=  1

# Contador  cresente de while

controle = 1

while controle <51:
      print(controle)
      controle += 1

# Exemplo de contagem decresente

controle = 100

while controle >  0:
      print(controle)
      controle -= 1

"""# Iterrompendo um laço"""

# Exemplo de interupção de um laço

for j in  range(10):
    if  j % 2 != 0: # condiçao de verdadeira
          print(j)
          break

"""# Um exemplo de interrupção de continue"""

# Exemplo de uso do continue

for w in range(10):
    if  w ==  1 or  w ==  8:
          continue
    print(

"""# Estruturas complexas em python - container

>tuplas

>listas

>dicionarios

# Tuplas

a tupla é um tipo de container que agrupa um conjunto de elementos.

Usamos parenteses para sua criação e separamos os elementos por vírgulas.

tuplas sao imutaveis, ou seja não podem ser modificadas
"""

# minha primeira tupla
# Crie uma tupla de exemplo com os elementos;
# Donots, sonho , pretzel , chocolate, bala de goma

padaria = ('Donots', 'sonho' , 'pretzel' , 'chocolate', 'bala de goma' )

print(padaria)

print(type(padaria))

total= len(padaria)

print(f'A tupla padaria tem {total} elemento')

"""Tuplas são imutaveis

Após sua criação não conseguimos modificar seus elementos


"""

# Tuplas são imutaveis

print(padaria)
print()
print(padaria[0]) # acessar o indice 1
print(padaria[1]) # acessar o indice 2
print(padaria[2]) # acessar o indice 3
print(padaria[3]) # acessar o indice 4
print(padaria[4])

print('A tupla antes de mudar')
print(padaria)
print()

padaria = ('Chiclete', 'sorvete' ,'pizza','pão de queijo','bolo')
print()
print(' A tupla padaria depois da alteraçao ')
print()
print(padaria)

"""# Operaçoes em tuplas

>Iterar pelos elementos

>ordenar

>contar os elementos

>indexar
"""

# @title Operaçoes em tuplas - interar elementos
for goroh in  padaria:
    print(goroh)

# @title Operaçoes em tuplas - sort

print(f'A tupla padaria antes de Ordenar é {padaria}.')

em_ordem = sorted(padaria)

print()

# @title Operações em tuplas - Contar elementos

print(padaria)

repetida  = padaria.count('pizza')
print(f'A palavra Pizza foi achada {repetida} vezes em padaria.')

# @title Operaçoes em tuplas - Indexar

aperitivo = padaria[2]

ondeesta  = padaria.index(aperitivo)

print(f'O elemento {aperitivo} esta na posição {ondeesta} da tupla.')

"""# Juntando todo : repetição, tuplas

Crie um progama que intera por todos os elementos de uma tupla e

exibe cada elemento e sua posição na tupla

"""

from re import I
print('inicio')

padaria = ('Chiclete', 'sorvete' ,'pizza','pão de queijo','bolo')

for i  in  range(0,  len(padaria)):
    print('o elemento %s da padaria esta na posiçao %i da tupla'%(padaria[i], i))

"""# Tuplas englobam dados de tipos diferentes"""

# Um exemplo abrangente

pessoa=('carlos', 'm', 60,1.73,82 True )
outrapessoa=('Onofre','m',33,1.89,121 False)

print(pessoa)

del(outra pessoa)
print(outrapessoa)

"""# Listas

A lista é um container que agrupo um conjunto de elementos,

acessados pelo seu indice

Listas são mutaveis, ou seja, podem ser modificadas.

listas podem conter zero ou mais elementos de um mesmo tipo

ou de tipo diferentes, incluindo outras listas.
"""

# @title Criando a primeira lista

l = [] #nossa primeira lista

print(f'a Lista l é {l}')
print()
print(f'O comprimento de l é {len(l)}')
print()
print(f'O tipo de l é {type(l)}')

# @title Alterando conteudo em uma lista
z = [15,8.3,900,-35]

print(z) # Exibir a lista original

print(z[0]) # Exibir o elemento 1
print(z[1]) # exibir o elemento 2
print(z[2]) # exibir o elemento 3

z[0]= 'joao'

print(z)

# Cuidado com as listas - cópias

lista_a= [1,2,3,4,5,6]


lista_b=lista_a   # uma "cópia" da lista original

print(lista_a)
print(lista_b)

lista_b[0] = 20 # alterando um valor da lista

print('lista_b', lista_b)

print('lista_a', lista_a)

"""# Declarando uma cópia da lista A


"""

lista_c = lista_a

print('lista_a',lista_a) print('lista_c',lista_c)

lista_c[0] = 15

print('lista_a',lista_a) print('lista_c',lista_c)

# @titlem Operaçoes com listas - interação

lanche_saudavel=['alface','cenoura','almeirão','chicoria','rucula','repolho']

print('ai que fome ')

for folha in  lanche_saudavel:
    print(folha)
print('\nUfa, to satisfeito')

# @title Operações com listas - ordenar e reverter

print('inicio do progama...\n')

itens=[2,3,5.5,-0.4,9,7,39,7,98,7]


print(f'Antes de ordenar: {itens}')

itens.sort()  # Ordenando a lista itens

print(f'A lista ordenaa :{itens}')

itens.reverse()

print(f'Formata a lista revertida: {itens}')

# @title operaçoes com lista - contar

contar = itens.count(7)

print(f'O numero de elementos {contar}')

# @title Operaçoes com listas - concatenar

maisistens = [3,4,7,13.2,25,8]

bando = itens + maisistens

print(bando)

bando2 = maisistens+itens

print(bando2)

#@title Adição de um novo elemento na lista

print(itens)
itens.reverse
print(itens)
itens.append(45)

print(itens)

# Exemplo interativo

numero = input('qualo numero para adicionar ')

itens.append(numero)

print(itens)

# @title Inserindo em uma posição específíca

print(itens)

itens.insert(4,10)  # insere na posição 4(indice) o valor 10

print(itens)

#@title Apagando um elemento

print(itens)
itens.remove(7)
print(itens)

# Um outro jeito de apagar uma lista

bando.clear()

print(bando)

"""Juntando tudo:

crie um progama que pesquise se um numero

existe em uma listagem

exiba a mensagem
"""

num=int(input('Veja se o numero consta '))

i=[7,9,10,12,34,89]

if  num==i:
    print('Seu numero consta')

elif num!=i:
      print('seu numero não consta ')

from _typeshed import Incomplete
from os import nice
# exemplo do professor

li =[7,9,12,34,104,89,1023]

p =int(input('Digite um numero '))
for n in  li
    in  n==p:
    print(f'O Elemto')