pergunta = int(input('Escolha o tipo de equação que voce irá Digitar: \n1 - aX+b=c\n2 - b+aX=c'))

if(pergunta == 1):
    equacao = input('Digite a equação').replace(' ', '')
    if(pergunta == 1):
        partes = equacao.split('=')
        c = int(partes[1])
        coeficiente = partes[0].split('x')
        a = int(coeficiente[0])
        b = int(coeficiente[1])
        x = (c-b)/a
        print('O valor de X é: ', x)
    else:
        print('Equação escrita errada!')

elif(pergunta == 2):
    equacao = input('Digite a equação').replace(' ', '')
    if(pergunta == 2):
        partes = equacao.split('=')
        c = int(partes[1])
        coeficiente = partes[0].split('+')
        a = int(coeficiente[1].replace('x',''))
        b = int(coeficiente[0])
        x = (c-b)/ a
        print('O valor de X é:', x)
    else:
        print('Equação escrita errada!')
else:
    print('Numero Digitado invalido não corresponde a nenhuma Equação')