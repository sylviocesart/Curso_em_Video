"""
Faça um programa que leia algo pelo
teclado e mostre na tela o seu tipo
primitivo e todas as informações
possíveis sobre elas

algo = input('Digite algo: ')
print(type(algo))
if algo.isnumeric():
    print('O valor digitado é numérico.')
elif algo.isalpha():
    print('Valor digitado é alpha.')
else:
    print('Valor digitado é alphanumérico')


algo = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Convertendo para maiúsculas', algo.upper())
print('Convertendo para minúsculas', algo.lower())
print('Está capitalizada?', algo.istitle())
"""

# Usando a nova sintaxe do python 3
algo = input('Digite algo: ')
print('"{}" -> O tipo primitivo desse valor é {}'.format(algo, type(algo)))
print('"{}" -> Só tem espaços? {}'.format(algo, algo.isspace()))
print('"{}" -> É um número? {}'.format(algo, algo.isnumeric()))
print('"{}" -> É alfabético? {}'.format(algo, algo.isalpha()))
print('"{}" -> É alfanumérico? {}'.format(algo, algo.isalnum()))
print('"{}" -> Está em maiúscula? {}'.format(algo, algo.isupper()))
print('"{}" -> Está em minúscula? {}'.format(algo, algo.islower()))
print('"{}" -> Convertendo para maiúsculas "{}"'.format(algo, algo.upper()))
print('"{}" -> Convertendo para minúsculas "{}"'.format(algo, algo.lower()))
print('"{}" -> Está capitalizada? {}'.format(algo, algo.istitle()))
