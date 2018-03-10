"""
Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu antecessor
"""
n = int(input('Digite um número: '))
an = n - 1
su = n + 1
print('O número digitado foi {}. Seu antecessor é {} e seu sucessor é {}'.format(n, an, su))
