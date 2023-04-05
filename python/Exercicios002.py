# 2 - Cria um algoritmo que leia um numero a mostra o seu dobro. triplo a raiz quadrada.

numero = float(input('Digite um numero ?'))
dobro = numero * 2
print('O dobro de {} é : {}'. format(numero, dobro))
triplo = numero * 3
print('O tripo de {} é : {}'.format(numero, triplo))
raiz = numero ** 0.5
if(raiz == int(raiz)):
    print('A raiz quadrada de {} é : {}'.format(numero, raiz))
else:
    print('{} não possui uma raiz exata, portanto a sua raiz fica: {}'.format(numero,raiz))
