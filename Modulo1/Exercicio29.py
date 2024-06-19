# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

Velocidade = int(input("Digite a velocidade do seu carro: "))
multa = (Velocidade - 80) * 7
if Velocidade > 80:
    print(f"Voce ultrapassou o limite de velocidade e terá que pagar {multa} reais")
else:
    print("Dirija com segurança")