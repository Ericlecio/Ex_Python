#Crie um programa que leia o nome da pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Qual é o seu nome completo ? "))
print(f"Seu nome tem silva ? {"SILVA" in nome.upper()}")