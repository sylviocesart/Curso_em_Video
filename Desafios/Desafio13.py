"""
Faça um algorítmo que leia o salário de um
funcionário e mostre seu novo salário com
15% de aumento.
"""
ju = int(input('Digite seu salário atual: '))
am = ju * 1.30
print('O seu salário atual de R$ {} reais teve um aumento de 30% e foi para R$ {:.0f} reais'.format(ju, am))
