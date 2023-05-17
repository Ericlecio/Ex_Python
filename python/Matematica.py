pergunta = int(input(
    'Escolha o tipo de equação que voce irá Digitar: \n1 - aX+b=c\n2 - b+aX=c\n3 - aX2 + bX + c = 0'))

if (pergunta == 1):
    equacao = input('Digite a equação').replace(' ', '')
    if (pergunta == 1):
        partes = equacao.split('=')
        c = int(partes[1])
        coeficiente = partes[0].split('x')
        a = int(coeficiente[0])
        b = int(coeficiente[1])
        x = (c-b)/a
        print('O valor de X é: ', x)
    else:
        print('Equação escrita errada!')

elif (pergunta == 2):
    equacao = input('Digite a equação').replace(' ', '')
    if (pergunta == 2):
        partes = equacao.split('=')
        c = int(partes[1])
        coeficiente = partes[0].split('+')
        a = int(coeficiente[1].replace('x', ''))
        b = int(coeficiente[0])
        x = (c-b) / a
        print('O valor de X é:', x)
    else:
        print('Equação escrita errada!')

elif (pergunta == 3):
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = ((b**2) - (4*a*c)) ** (1/2)
    x1 = (- b + delta)/2
    x2 = (- b - delta)/2
    print('X1=', x1)
    print('X2=', x2)
else:
    print('Numero Digitado invalido, não corresponde a nenhuma Equação')
