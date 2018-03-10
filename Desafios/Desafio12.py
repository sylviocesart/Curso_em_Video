"""
Faça um algorítmo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto
"""
preco = int(input('Digite o preço: '))
desc5per = (preco * 1.05) - preco
preco_final = preco - desc5per
print('O valor de R$ {} reais, com desconto de 5% fica R$ {:.0f} reais.'.format(preco, preco_final))