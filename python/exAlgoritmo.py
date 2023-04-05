# ---------------------------------------------------------- EXERCÍCIOS FÁCEIS ---------------------------------------------------

# 1 - Considere a seguinte string>
# texto = 'O rato roeu a roupa do rei de roma'

# a) Escreva um código que imprima a string em letras maiúsculas.
#print('letras maiusculas: ', texto.upper())

# b) Escreva um código que imprima a string em letras minúsculas.
#print('letras minusculas: ', texto.lower())

# c) Escreva um código que imprima a quantidade de caracteres da string.
#print('letras maiusculas: ', len(texto), 'caracteres')

# d) Escreva um código que substitua a palavra "rei" por "rainha" na string.
# print(texto.replace('rei','rainha'))

# e) Escreva um código que imprima o número de ocorrências da letra "o" na string.
# print(texto.count('o'))


# 2 - Considere a seguinte lista de números:
# numeros = [10, 5, 8, 20, 15, 30, 25, 12]

# a) Escreva um código que imprima os números da lista em ordem crescente.
# numeros.sort()
# print(numeros)

# b) Escreva um código que imprima os números da lista em ordem decrescente.
# numeros.sort(reverse=True)
# print(numeros)

# c) Escreva um código que calcule a média dos números da lista.
# soma = sum(numeros)
# print(soma/len(numeros))

# d) Escreva um código que encontre o maior número da lista e o imprima.
# print(max(numeros, key=int))

# e) Escreva um código que encontre o menor número da lista e o imprima.
# print(min(numeros, key=int))


# 3 - Considere a seguinte lista de tuplas, cada uma representando um produto e seu respectivo preço:
# produtos = [("Camisa", 29.99), ("Calça", 59.99), ("Meia", 9.99), ("Tênis", 99.99), ("Boné", 19.99)]

# a) Escreva um código que imprima apenas os nomes dos produtos, sem os preços.
# for nomes in produtos:
#     nomes += produtos[0]
#     print(nomes[0])


# b) Escreva um código que imprima apenas os preços dos produtos, sem os nomes.
# for preco in produtos:
#    preco += produtos[0]
# print(preco[1])

# c) Escreva um código que calcule o preço médio dos produtos.
# soma = 0
# for preco in produtos:
#    preco += produtos[0]
#    soma += preco[1]
# print(soma/len(produtos))

# d) Escreva um código que encontre o produto mais caro da lista e imprima seu nome e preço.

# maior = max(produtos)
# print(maior)


# 4 - Considere o seguinte dicionário de telefones:
# telefones = {"João": "1111-1111", "Maria": "2222-2222", "Pedro": "3333-3333", "Ana":  "4444-4444", "Lucas": "5555-5555"}

# a) Escreva um código que imprima todos os nomes das pessoas que estão no dicionário.
# nomes = telefones.keys()
# print(nomes)

# b) Escreva um código que imprima todos os telefones das pessoas que estão no dicionário.
# telefones = telefones.values()
# print(telefones)

# c) Escreva um código que imprima o telefone da pessoa "Pedro".
# pedro = telefones['Pedro']
# print(pedro)

# d) Escreva um código que adicione o telefone "7777-7777" para a pessoa "Marcos".
# telefones['Marcos'] = "7777-7777"
# print(telefones)


# e) Escreva um código que remova a pessoa "Ana" do dicionário.
# telefones.pop('Ana')
# print(telefones)


# 5 - Considere os seguintes conjuntos de números:
# A = {1, 2, 3, 4, 5}
# B = {3, 4, 5, 6, 7}
# C = {4, 5, 6, 7, 8}

# a) Escreva um código que imprima a união entre os conjuntos A e B.
# print(A.union(B))

# b) Escreva um código que imprima a interseção entre os conjuntos B e C.
# print(B.intersection(C))

# c) Escreva um código que imprima a diferença entre os conjuntos A e B.
# print(set(A) - set(B))

# d) Escreva um código que imprima a diferença simétrica entre os conjuntos B e C.
# print(set(B) ^ set(C))

# e) Escreva um código que verifique se o número 2 está no conjunto A.
# print(2 in set(A))

# f) Escreva um código que verifique se o conjunto B é subconjunto do conjunto C.
# print(set(B) < set(C))


# ------------------------------------------------------------- FIM EXERCÍCIOS FÁCEIS ------------------------------------------------
# --------------------------------------------------------------EXERCÍCIOS INTERMEDIÁRIOS --------------------------------------------

# 1. Considere a seguinte string:
texto = "Um passarinho me contou que viu um gato de botas tomando um café com um pinguim"


# a) Escreva um código que imprima todas as palavras da string em ordem alfabética, sem repetição.
# frases = [frase for frase in texto.split()]
# frases.sort()
# print(frases)

# b) Escreva um código que conte quantas vezes a letra "a" aparece no texto (não diferencia maiúsculas de minúsculas).
#print(texto.count('a'))

# c) Escreva um código que imprima todas as palavras do texto em ordem alfabética, com a primeira letra em maiúscula.
# frases = [frase for frase in texto.split()]
# frases.sort()
# string = " ".join(frases)
# print(string.title())

# d) Escreva um código que imprima todas as palavras do texto em ordem decrescente de tamanho.
