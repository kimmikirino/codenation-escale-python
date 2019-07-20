# dada a lista de linguagens imprima na tela a linguagem que começa com a letra p   
# linguagens = ['Java', 'PHP', 'C', 'Python']

# for linguagem in linguagens:
#     if linguagem.upper().startswith('P') :
#         print(linguagem)

# message = ''

# while message != 'quit':
#     message = input('Digite sua mensagem: ')
#     print(message)

# counter = 1
# total = 0
# while counter <= 3:
#     num = int(input('Digite um numero: '))
#     total = total + num
#     counter += 1
# print(total)

# while True:
#     message = input('Digite sua mensagem: ')
#     if message == 'sair':
#         break

# print(message)

# count = 1
# total = 0
# while count <= 3:
#     total += int(input('Digite um numero: '))
#     count += 1
# print(total)

# def greet_user(name):
#     print(f'Olá, {name}')

# greet_user('Jaqueline')
# greet_user(name='Jaqueline')

# #typing hinting
# def get_full_name(first_name:str, last_name: str):
#     print(f'{first_name} {last_name}').title()

# movies = [('Capitã Marvel', 2019), ('Pantera Negra', 2018), ('Dr Estranho', 2016), ('Thor', 2017)]

# def convert_to_obj(list_data: str) -> dict:
#   obj = {}
#   for item in list_data:
#     obj[item[1]] = item[0]
#   print(obj)
#   return 'ola'

# print(convert_to_obj(movies))

# def make_pizza(*toppings):
#   print(toppings)

# make_pizza('pepperoni')
# make_pizza('pepperoni', 'queijo', 'loucura', 'salame')

# # argumentos dinamicos

# def sanduiche(*recheios):
#   print('Resumo do sanduiche: ')
#   for recheio in recheios:
#     print(recheio)

# ingredients = ['pao', 'hamburguer', 'salad']
# sanduiche('alo', 'alo2')
# sanduiche(ingredients)

# # argumentos nomeados arbitrarios
# def build_profile(first_name, last_name, **info): # sempre dicionario
#   profile = {}
#   profile['first'] = first_name
#   profile['last'] = last_name
#   # print(info)
#   for key, value in info.items():
#     profile[key] = value
#   print(profile)
#   return profile

# build_profile('jaqueline', 'kirino', age=32, secondname='kimmi')

# exercicio
# escreva uma função que armazene informações sobre um celualr
# a função sempre deve receber um modela e a marca
# um numero arbitrario de argumentos nomeados então deve ser aceito


# def cellphone(model, brand, **info):
#   cell = {
#     'model': model,
#     'brand': brand
#   }
#   for key, value in info.items():
#     cell[key] = value
#   return cell

# print(cellphone('X', 'apple', screen='10cm', camera=True, size='100gb'))

# classe conta bancaria

class Conta:
  def __init__(self, **args):
    self.banco = args['banco']
    self.agencia = args['agencia']
    self.conta = args['conta']
    self.nome = args['nome']
    self.saldo = 0
  
  def sacar(self, valor):
    self.saldo -= valor

  def depositar(self, valor):
    self.saldo += valor

  def getSaldo(self):
    return self.saldo

conta_bancaria = Conta(banco='itau', agencia=10, conta=1002, nome='jaqueline')
print(conta_bancaria.banco)
print(conta_bancaria.saldo)
conta_bancaria.depositar(100)
print(conta_bancaria.getSaldo())
conta_bancaria.sacar(5)
print(conta_bancaria.saldo)

class ContaPF(Conta):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.cpf = kwargs['cpf']

class ContaPJ(Conta):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.cnpj = kwargs['cnpj']

  def sacar(self, valor):
    super().sacar(valor)
    # para debugar
    # import pdb; pdb.set_trace()
    self.saldo -= 1


contaPF = ContaPF(banco='itau', agencia=10, conta=1002, nome='jaqueline', cpf=555444444)
print(contaPF.cpf)
print(contaPF.saldo)
contapessoaJuridica = ContaPJ(banco='itau', agencia=10, conta=1002, nome='jaqueline', cnpj=555444444)
contapessoaJuridica.depositar(1000)
print(contapessoaJuridica.saldo)
contapessoaJuridica.sacar(10)
print(contapessoaJuridica.saldo)