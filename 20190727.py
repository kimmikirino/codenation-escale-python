# List comprehension
# old_list = []
# new_list = [expression(item) for item in old_list]

# equivalente
# for item in old_list:
#     new_list.append(item)

# {f: len(f) for f in fruits}

# linguagens = ['Java', 'PHP', 'C', 'Python']
# new_list = []
# new_list = [linguagem.upper() for linguagem in linguagens if linguagem.startswith('P')]

# print(new_list)

# new_list2 = [linguagem.upper() if linguagem.startswith('P') else 'não começa com P' for linguagem in linguagens ]

# print(new_list2)

# Modulos e packages
# # arquivos py

## decorators

# def banana(funcao):
#     def wrapper():
#         print('alo')
#         funcao()
#         print('alo2')
    
#     return wrapper

# def maca(a):
#     def wrapper():
#         print('maca')
        
#     return wrapper

# @maca
# @banana
# def outra_funcao():
#     print('sou um argumento')

# @banana
# def alos():
#     print('dius')

# # entra primeiro no decoratpor e passa por parametro
# outra_funcao() 
# alos()

# pip install requests