"""
Faça um programa que leia um número
inteiro qualquer e mostre na tela
sua tabuada
"""
n = int(input('Digite um número: '))
cont = 1
while cont <= 9:
    m = n * cont
    print('{} x {} = {}'.format(n, cont, m))
    cont += 1
