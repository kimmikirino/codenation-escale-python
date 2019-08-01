
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError: 
        return 0
    except TypeError:
        return 'Não é possível dividir '

print(divide(10, 2))
print(divide(10, 0))
print(divide('a', 0))