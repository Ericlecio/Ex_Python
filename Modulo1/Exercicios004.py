# 4 - Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

valorEmMetros = float(input('Digite o valor em metros: '))
centimetros = valorEmMetros * 100
milimetros = valorEmMetros * 1000
print(' O valor de {} em centimetros fica {} e em milimetros fica {}'.format(valorEmMetros,centimetros, milimetros))
