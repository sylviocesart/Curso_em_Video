"""
Entre com um nome e mostre uma mensagem de boas
vindas
"""
nome = input('Digite seu nome: ')
print('É um prazer te conhecer,', nome,'!')

# Outra forma de imprimir o resultado
print('É um prazer te conhecer, %s!' %(nome))

# Mais uma forma de imprimir o resultado
print('É um prazer te conhecer, {}!'.format(nome))
