# 6 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar considere US$1,00 = 3.27

dinheiro = float(input('Quanto dinheiro você tem na carteira ?'))
converter = dinheiro / 3.27
print('Você pode comprar US${}'.format(converter))
