# # ---------------------------------------------------------- EXERCÍCIOS FÁCEIS ---------------------------------------------------

# # 1 - Considere a seguinte string>
# texto = 'O rato roeu a roupa do rei de roma'

# # a) Escreva um código que imprima a string em letras maiúsculas.
# print('letras maiusculas: ', texto.upper())

# # b) Escreva um código que imprima a string em letras minúsculas.
# print('letras minusculas: ', texto.lower())

# # c) Escreva um código que imprima a quantidade de caracteres da string.
# print('letras maiusculas: ', len(texto), 'caracteres')

# # d) Escreva um código que substitua a palavra "rei" por "rainha" na string.
# print(texto.replace('rei','rainha'))

# # e) Escreva um código que imprima o número de ocorrências da letra "o" na string.
# print(texto.count('o'))


# # 2 - Considere a seguinte lista de números:
# numeros = [10, 5, 8, 20, 15, 30, 25, 12]

# # a) Escreva um código que imprima os números da lista em ordem crescente.
# numeros.sort()
# print(numeros)

# # b) Escreva um código que imprima os números da lista em ordem decrescente.
# numeros.sort(reverse=True)
# print(numeros)

# # c) Escreva um código que calcule a média dos números da lista.
# soma = sum(numeros)
# print(soma/len(numeros))

# # d) Escreva um código que encontre o maior número da lista e o imprima.
# print(max(numeros, key=int))

# # e) Escreva um código que encontre o menor número da lista e o imprima.
# print(min(numeros, key=int))


# # 3 - Considere a seguinte lista de tuplas, cada uma representando um produto e seu respectivo preço:
# produtos = [("Camisa", 29.99), ("Calça", 59.99), ("Meia", 9.99), ("Tênis", 99.99), ("Boné", 19.99)]

# # a) Escreva um código que imprima apenas os nomes dos produtos, sem os preços.
# for nomes in produtos:
#     nomes += produtos[0]
#     print(nomes[0])


# # b) Escreva um código que imprima apenas os preços dos produtos, sem os nomes.
# for preco in produtos:
#    preco += produtos[0]
# print(preco[1])

# # c) Escreva um código que calcule o preço médio dos produtos.
# soma = 0
# for preco in produtos:
#    preco += produtos[0]
#    soma += preco[1]
# print(soma/len(produtos))

# # d) Escreva um código que encontre o produto mais caro da lista e imprima seu nome e preço.
# maior = max(produtos)
# print(maior)


# # 4 - Considere o seguinte dicionário de telefones:
# telefones = {"João": "1111-1111", "Maria": "2222-2222", "Pedro": "3333-3333", "Ana":  "4444-4444", "Lucas": "5555-5555"}

# # a) Escreva um código que imprima todos os nomes das pessoas que estão no dicionário.
# nomes = telefones.keys()
# print(nomes)

# # b) Escreva um código que imprima todos os telefones das pessoas que estão no dicionário.
# telefones = telefones.values()
# print(telefones)

# # c) Escreva um código que imprima o telefone da pessoa "Pedro".
# pedro = telefones['Pedro']
# print(pedro)

# # d) Escreva um código que adicione o telefone "7777-7777" para a pessoa "Marcos".
# telefones['Marcos'] = "7777-7777"
# print(telefones)


# # e) Escreva um código que remova a pessoa "Ana" do dicionário.
# telefones.pop('Ana')
# print(telefones)


# # 5 - Considere os seguintes conjuntos de números:
# A = {1, 2, 3, 4, 5}
# B = {3, 4, 5, 6, 7}
# C = {4, 5, 6, 7, 8}

# # a) Escreva um código que imprima a união entre os conjuntos A e B.
# print(A.union(B))

# # b) Escreva um código que imprima a interseção entre os conjuntos B e C.
# print(B.intersection(C))

# # c) Escreva um código que imprima a diferença entre os conjuntos A e B.
# print(set(A) - set(B))

# # d) Escreva um código que imprima a diferença simétrica entre os conjuntos B e C.
# print(set(B) ^ set(C))

# # e) Escreva um código que verifique se o número 2 está no conjunto A.
# print(2 in set(A))

# # f) Escreva um código que verifique se o conjunto B é subconjunto do conjunto C.
# print(set(B) < set(C))


# # ------------------------------------------------------------- FIM EXERCÍCIOS FÁCEIS ------------------------------------------------
# # --------------------------------------------------------------EXERCÍCIOS INTERMEDIÁRIOS --------------------------------------------

# # 1. Considere a seguinte string:
texto = "Um passarinho me contou que viu um gato de botas tomando um café com um pinguim"

# # a) Escreva um código que imprima todas as palavras da string em ordem alfabética, sem repetição.
# texto.lower()
# frases = texto.split()
# frases1 = sorted(frases)
# for palavras in frases1:
#     print(palavras)


# # b) Escreva um código que conte quantas vezes a letra "a" aparece no texto (não diferencia maiúsculas de minúsculas).
# print(texto.count('a'))

# # c) Escreva um código que imprima todas as palavras do texto em ordem alfabética, com a primeira letra em maiúscula.
# frases = [frase for frase in texto.split()]
# string = " ".join(frases)
# print(string.title())

# # d) Escreva um código que imprima todas as palavras do texto em ordem decrescente de tamanho.
frases = [frase for frase in texto.split()]
palavras = sorted(frases, key=len, reverse=True)
for palavra in palavras:
    print(palavra)


# # 2 - Explique o resultado do código abaixo:

# lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# soma = sum([num for sublist in lista for num in sublist])
# print(soma)

# # R. No codigo temos uma exemplos de listas dentro de lista, ao todo temos 3 sublista, cada sublista corresponde a uma posição da lista principal, a varivel soma é atribuida a funcao 'SUM' que serve pra somar os elementos, enquanto utiliza o for para percorrer as sublista dentro da lista principal e somas todos os valores contido nas tres sublistas.


# # 3 - Considere a seguinte tupla:

tupla = (1, 2, 3, [4, 5, 6])
# # a) Explique o resultado de uma operação que tenta modificar o terceiro elemento da lista dentro da tupla. Ex:
tupla[3][0] = 7
print(tupla)

# # R. A questão ja nos da a resposta da pergunta, temos uma tupla que contem 4 elementos, e o elemento 4 é uma lista que contem 3 elementos. tentamos modificar o elemento 0 da lista, pois lista são mutaveis, mesma ela estando dentro de uma tupla que é imutavel. mas se tentamos mudar os elementos das que estão dentro da tupla o codigo não iria funcionar.

# # b) Explique o resultado de uma operação que modifica o terceiro elemento da listadentro da tupla. Ex:
# tupla[3][0].append(7)
# print(tupla)

# # R. No codigo ocorre um erro pois ao colocar o append que é um metodo para adicionar elementos dentro de lista, o usuario especificou a posicao '[0]' dentro da lista, o que não é necessario, so precisando especificar o lista que neste caso é [3].
# # O codigo correto neste casos seria:
# tupla[3].append(7)
# print(tupla)


# # 4. Considere o seguinte dicionário
# estoque = {
#     "produto1": {
#         "nome": "Camisa",
#         "preco": 50.0,
#         "quantidade": 100,
#         "tamanhos": ["P", "M", "G"]
#     },
#     "produto2": {
#         "nome": "Calça",
#         "preco": 80.0,
#         "quantidade": 50,
#         "tamanhos": ["38", "40", "42", "44"]
#     },
#     "produto3": {
#         "nome": "Tênis",
#         "preco": 120.0,
#         "quantidade": 20,
#         "tamanhos": ["39", "40", "41", "42", "43", "44"]
#     }
# }
# # Qual o código Python que pode ser utilizado para obter uma lista com todos os tamanhos disponíveis para todos os produtos no estoque, sem repetições?

# tamanhos_disponiveis = set() 

# for produto in estoque.values(): 
#     tamanhos_disponiveis.update(produto["tamanhos"]) 

# print(list(tamanhos_disponiveis))