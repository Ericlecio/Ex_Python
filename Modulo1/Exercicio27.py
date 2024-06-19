# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Qual é o seu nome completo ? ")).strip()
nome = n.split() #split divide as palavras dentro de uma string para dentro de uma lista
print(f"Seu primeiro nome é: {nome[0]}")
print(f"Seu ultimo nome é: {nome[len(nome)-1]}")