"""
Tipos primitivos e saídas de dados
"""
n1 = input('Digite um número: ')
print(type(n1))

n2 = int(input('Digite um número: '))
print(type(n2))

# Somando dois números e utilizando o novo formato para o python3
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
