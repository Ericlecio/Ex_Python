# 5 - Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada. 

numero = int(input('Digite um numero de 0 a 10: '))
cont = 0
for cont in range(11):
    print('{} * {} = {}' . format(numero, cont, numero*cont))
    cont = cont + 1
