# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira foi {}'.format(num, math.trunc(num)))