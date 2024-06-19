# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5) #faz o computador pensar
print("-=-" * 20)
print("Vou pensar em um numero, tente adivinhar")
print("-=-"* 20)
jogador = int(input("Em que numero eu pensei ? "))
if jogador == computador:
    print("Parabens voce acertou o numero que eu pensei :)")
else:
    print("Errouuu")