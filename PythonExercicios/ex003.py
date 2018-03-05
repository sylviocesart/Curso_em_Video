"""
Crie um script que leia dois números e tente
mostrar a soma entre eles
"""
# Primeiro vamos mostrar uma "soma errada", onde será feito apenas a junção dos números
num1 = input('Digite um valor: ')
num2 = input('Digite outro valor: ')
soma = num1 + num2
print('A soma entre {} e {} é igual a {}!'.format(num1, num2, soma))

# Agora, mostrando a soma realmente dos números
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
soma = num1 + num2
print('A soma entre {} e {} é igual a {}!'.format(num1, num2, soma))
