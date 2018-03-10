"""
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
Dólares ela pode comprar

Considere US$ 1,00 = R$ 3,27
"""
dolar = 3.27
print('\nAtualmente o valor do dólar é: {}\n'.format(dolar))
valor = float(input('Quanto de dinheiro você tem na carteira? '))
qnt_dolar = valor // 3.27
qnt_centavos = valor % 3.27
menor_dolar = valor / 3.27

if valor < 3.27:
    print('Valor mínimo para se comprar um dólar é {}'.format(dolar))
    print('Com esse valor, você só consegue comprar {:.2f} centavos de dólar.'.format(menor_dolar))
else:
    if qnt_dolar == 1:
        if qnt_centavos == 0:
            print('Com o valor de R$ {}, você consegue comprar {} dólar.'.format(valor, qnt_dolar))
        else:
            print('Com o valor de R$ {}, você consegue comprar {} dólar e {:.2f} centavos de dólar.'.format(valor, qnt_dolar, qnt_centavos))
    elif qnt_dolar > 1:
        if qnt_centavos == 0:
            print('Com o valor de R$ {}, você consegue comprar {} dólares.'.format(valor, qnt_dolar))
        else:
            print('Com o valor de R$ {}, você consegue comprar {} dólares e {:.2f} centavos de dólar.'.format(valor, qnt_dolar, qnt_centavos))
