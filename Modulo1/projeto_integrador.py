import random

def soma():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)  
    operacao = random.choice(['+'])
    expressao = f"{numero1} {operacao} {numero2}"

    print("="*60)
    pergunta = int(input(f"Quanto é {expressao} ? "))
    resultado = eval(expressao)
    # print(format(resultado, ".2f"))
    if (pergunta == resultado):
        print('Voce acertou o resultado da operação é: ',format(resultado, ".2f"))
    else:
        print('Resposta incorreta. O resultado correto é:',format(resultado, ".2f"))

def adicao():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)  
    operacao = random.choice(['-'])
    expressao = f"{numero1} {operacao} {numero2}"

    print("="*60)
    pergunta = int(input(f"Quanto é {expressao} ? "))
    resultado = eval(expressao)
    # print(format(resultado, ".2f"))
    if (pergunta == resultado):
        print('Voce acertou o resultado da operação é: ',format(resultado, ".2f"))
    else:
        print('Resposta incorreta. O resultado correto é:',format(resultado, ".2f"))

def multiplicação():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)  
    operacao = random.choice(['*'])
    expressao = f"{numero1} {operacao} {numero2}"

    print("="*60)
    pergunta = int(input(f"Quanto é {expressao} ? "))
    resultado = eval(expressao)
    # print(format(resultado, ".2f"))
    if (pergunta == resultado):
        print('Voce acertou o resultado da operação é: ',format(resultado, ".2f"))
    else:
        print('Resposta incorreta. O resultado correto é:',format(resultado, ".2f"))

def divisao():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)  
    operacao = random.choice(['/'])
    expressao = f"{numero1} {operacao} {numero2}"

    print("="*60)
    pergunta = int(input(f"Quanto é {expressao} ? "))
    resultado = eval(expressao)
    # print(format(resultado, ".2f"))
    if (pergunta == resultado):
        print('Voce acertou o resultado da operação é: ',format(resultado, ".2f"))
    else:
        print('Resposta incorreta. O resultado correto é:',format(resultado, ".2f"))

def aleatorios():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)

    operacao = random.choice(['+', '-', '/', '*'])
    expressao = f"{numero1} {operacao} {numero2}"

    print("="*60)
    pergunta = int(input(f"Quanto é {expressao} ? "))
    resultado = eval(expressao)
    # print(format(resultado, ".2f"))
    if (pergunta == resultado):
        print('Voce acertou o resultado da operação é: ',format(resultado, ".2f"))
    else:
        print('Resposta incorreta. O resultado correto é:',format(resultado, ".2f"))


def valorX():
    x1 = random.randint(0, 100)
    x2 = random.randint(0, 100)

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
        print("1. Descobrir valor de X")
        print("2. Operações aleatorias")
        print("3. Soma")
        print("4. Adição")
        print("5. Multiplicação")
        print("6. Divisão")
        print("7. Sair")
        opcoes = input("Opção: ")

        if opcoes == "1":
            valorX()
        elif opcoes == "2":
            aleatorios()
        elif opcoes == "3":
            soma()
        elif opcoes == "4":
            adicao()
        elif opcoes == "5":
            multiplicação()
        elif opcoes == "6":
            divisao()
        elif opcoes == "7":
            print("="*60)
            print("Programa encerrado! OBRIGADO POR TESTAR :) ")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")


if __name__ == "__main__":
    main()