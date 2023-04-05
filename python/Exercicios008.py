# 8 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Digite o preço do produto: '))
novo = produto - (produto*5/100)
print('O preco do produto com 5% de desconto sera: {}'.format(novo))
