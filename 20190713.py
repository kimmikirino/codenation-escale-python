# name = input('Qual o seu nome?')
# print('olá %s' %name)
# print(f'olá {name}')
# print('olá {}'.format(name))

# palavras reservadas
# import keyword
# print(keyword.kwlist)

# snake nome_completo

# tipo de dados
# string, int, float, complex, bool

# email = 'aaaa@aaa.com'
# print(type(email)) # str

# age = 10
# print(type(age)) # int

# price = 3.0
# print(type(price)) # float

# complex_value = 3 + 6j
# print(type(complex_value)) # numeros irracionais, complex

# has_food = True
# print(type(has_food)) # bool

# print('abacate'.upper()) # maiuscula
# print('Jao da SilvaAAAAA'.lower()) # minuscula
# print('kimmi kirino'.capitalize()) # primeira letra maiuscula
# print('kimmi kirino'.title()) # primeira letra de cada palavra da string

# string como array
# bolo = 'bolo de cenoura'
# print(bolo[0]) # posição 0 = b
# print(bolo[-2]) # posição de tras para frente = r
# print(bolo[:3]) # os tres primeiros = bol
# print(bolo[1:4]) # os primeiros = bolo 
# print(bolo[0:6:2]) # pega a posição zero e pula de dois em dois até a 6 = bl
# print(bolo[::-1]) # inverte a string

# replace 
# print('string'.replace('i', 'o')) # strong
# print('string'.find('i')) # retorna index
# print('string'.find('i', 1)) # retorna index, segundo parametro é onde inicia
# print('banana'.find('i')) # retorna index -1 quando não encontra

# Data Types
# Exerício, defina as variaveis e verifique os tipos
# nome = 'Jaqueline'
# idade = 32
# nota = 8.75
# aprovada = True

# print(type(nome)) # str
# print(type(idade)) # int
# print(type(nota)) # float
# print(type(aprovada)) # bool

# exercicio 2
# serie = 'stranger things'
# print(serie.upper()) # defina em maiúsculo
# print(serie.title()) # primeira letra de cada maiusculo
# print(serie[::-1]) # palavra invertida

# comandos uteis
# len() 
# nome = 'Jaqueline'
# print(len(nome)) # 9
# print(dir(nome)) # dir lista tudo que é possível usar na variavel nome, que no caso é string
# help(str) # mostra a descrição da function builtin

# numero = 10
# print(str(numero)) # converte para string
# print(numero.__str__()) # converte para string

# id() mostra o endereço da memória onde a variavel está armazenada
# jaq = 10
# print(id(numero)) # mesmo endereço na memoria por ter o mesmo valor (mas não grande)
# print(id(10)) # mesmo endereço na memoria
# print(id(jaq)) # mesmo endereço na memoria

# lista, tupla, dicionario, set
# lista = [1,'2','farinha','4']
# tupla = (1,2,3,4)
# dicionario = {'nome': 'Maria'}
# conjunto = {1, 2, 4}

# lista.append('fermento')
# print(lista)
# # para adicionar elemento
# # lista.append(['pão', 'queijo'])
# # print(lista[5][0])
# lista[0] = 'relógio'
# print(lista)

# listaStr = ' : '.join(lista) # so funciona quando tiver só string
# print(listaStr)

# Tupla - normalmente são dados imutaveis, nao é possivel alterar seus dados

# dicionario
# dicionario = {
# "nome": "aloha",
# "idade": "3",
# 'linguagem': 'python'
# }
# print(dicionario["nome"])
# del dicionario['idade']
# valor = dicionario.pop('linguagem') # remove um item e armazena no valor
# dicionario["data"] = 'ae'
# print(valor)
# print(dicionario)
# print(dicionario.items()) # array com tuplas
# print(dicionario.values()) # array com os valores
# print(dicionario.keys()) # array so as chaves

# dicio = dicionario
# dicio['nome'] = 'jax'
# print(dicionario)
# print(dicio) # pega por referencia

# # conjuntos
# conjunto1 = { 1, 2, 3, 4, 5}
# conjunto2 = { 1, 9, 8, 7, 5}
# print(conjunto1 - conjunto2) # ele retorna tudo q tem no um mas nao tem no dois = 2,3,4
# print(conjunto1.intersection(conjunto2)) # numeros em comum 1, 5

# # Dado a Lista, adicione cha na lista de bebidas
# itens = ['coxinha', 'bolo', ['refri', 'suco'], 'doce']
# itens[2].append('chá')
# print(itens)

# Operations

a = 2
b = 3
c = 2.0
d = '2.0'

# resto %, potencia **, divisao /, soma +, menos - , 
# print(a + b)
# print(b ** a)
# print(a + c)
# print(a + float(d))

# print(2**3) # dois ao cubo

# operadores logicos
# or , and 
# nota_p1, nota_p2, nota_p3 = 5, 6, 8

# media = (nota_p1 + nota_p2 + nota_p3 ) / 3

# print(a == c)
# print(a < b and b < c)
# print(a > c or a >= c)
# print(not(a != b and b <=(a**2)-1))

# condicionais

number = int(input('Manda teu numero ai mano '))
signal = 'positivo'
if number < 0:
  signal = 'negativo'

if number % 2 == 0:
  print(f'é par e {signal}')
else :
  print(f'é impar e {signal}')

  ## beatriz.uezo

