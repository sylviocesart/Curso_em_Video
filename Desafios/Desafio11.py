"""
Faça um programa que leia a largura e altura
de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la.
Sabe-se que cada litro de tinta pinta uma área de 2 m2
"""
largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
area = largura * altura
qnt_tinta = area / 2
print('A sua parede com as dimensões dadas de {}m de altura e {}m de largura.'.format(altura, largura))
print('Tem uma área de {} m2. Sendo assim, será necessário {} litros de tinta para pintá-la.'.format(area, qnt_tinta))
