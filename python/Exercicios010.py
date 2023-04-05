# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangula retangulo, calcule e mostre o comprimento da hipotenusa.

# catetoOposto = float(input('Comprimento do cateto oposto: '))
# catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
# hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
# print('A hipotenusa vai media {:.2f}'.format(hipotenusa))




# Com importação
import math

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoOposto,catetoAdjacente)
print('A hipotenusa vai media {:.2f}'.format(hipotenusa))

