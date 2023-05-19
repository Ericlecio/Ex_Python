import random


def calculos():
    numero1 = random.randint(1, 100)
    numero2 = random.randint(1, 100)

    operacao = random.choice(['+', '-', '/', '*'])
    expressao = f"{numero1} {operacao} {numero2}"

    print("="*60)
    pergunta = int(input(f"Quanto é {expressao} ? "))
    resultado = eval(expressao)
    print(format(resultado, ".2f"))
    if (pergunta == resultado):
        print('Voce acertou o resultado da operação é: ',format(resultado, ".2f"))
    else:
        print('Resposta incorreta. O resultado correto é:',format(resultado, ".2f"))


def valorX():
    x1 = random.randint(1, 100)
    x2 = random.randint(1, 100)

    operacao = random.choice(['+', '-', '*'])
    expressao = f"{x1} {operacao} {x2}"
    resultado = eval(expressao)
    print("="*60)

    valorx = int(input(f"Qual é o valor de X nessa operação x {operacao} {x2} = {resultado} ? "))
    resultado = eval(expressao)

    if (x1 == valorx):
        print('Você Acertou!, O valor de X é: ', x1)
    else:
        print('Resposta incorreta. O valor correto de X é: ', format(x1, ".2f"))


def main():
    print("Programas de matemática \n")

    while True:
        print("="*60)
        print("Escolha uma opção: ")
        print("1. Começar")
        print("2. Descobrir valor de X")
        print("3. Sair")
        opcoes = input("Opção: ")

        if opcoes == "1":
            calculos()
        elif opcoes == "2":
            valorX()
        elif opcoes == "3":
            print("="*60)
            print("Programa encerrado! OBRIGADO POR TESTAR :) ")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")


if __name__ == "__main__":
    main()
