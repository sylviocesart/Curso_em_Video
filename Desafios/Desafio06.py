"""
Crie um algoritmo que leia um número e mostre
o seu dobro, triplo e raiz quadrada
"""
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
# rz = n ** (1/2)
# Raiz quadrada usando a funcao pow
rz = pow(n, (1/2))
print('O número digitado foi: {}. O dobro dele é {}'.format(n, d), end=' ')
print('e o triplo é {} e a raiz quadrada é {:.2f}'.format(t, rz))
