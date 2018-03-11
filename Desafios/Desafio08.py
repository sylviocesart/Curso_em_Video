"""
Escreva um programa que leia um valor
em metros e o exiba convertido em centimetros
e em milimetros
"""
n = float(input('Digite um valor em metros: '))
cent = n * 100
mili = n * 1000
print('O valor de {} metros, corresponde a {} centimetros e em {} milimetros'.format(n, cent, mili))
