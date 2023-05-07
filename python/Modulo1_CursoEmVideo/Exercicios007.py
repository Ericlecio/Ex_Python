# 7 - Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta , pinta uma area de 2m2

largura = float(input('Largura da parede: '))
altura = float(input('altura da parede: '))
area = altura * largura
tinta = area/2
print('A parede possui are de {}m2 /n A quantidade de tinta necessaria para pintar sera de {}l'.format(area,tinta))
