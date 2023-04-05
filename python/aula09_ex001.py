# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiusculas.
# 2 - O nome com todas as minusculas.
# 3 - Quantas letras ao todo (Sem considerar os espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Digte o seu nome e sobrenome: '))
print('O nome com as letras maiusculas é: ', nome.upper())
print('O nome com as letras minusculas é: ', nome.lower())
print('Quantidade de letras sem considerar os espaços: ', len(nome.strip()),'letras')
print('O primeiro nome possui: ', len(nome[:9]), 'letras')
