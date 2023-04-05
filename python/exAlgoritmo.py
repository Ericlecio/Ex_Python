# 1 - Considere a seguinte string>

texto = 'O rato roeu a roupa do rei de roma'


#a) Escreva um codigo que imprima a string em letras maiusculas.
print('letras maiusculas: ',texto.upper())


#b)minuscula
print('letras minusculas: ',texto.lower())


#c) quantidade
#print('letras maiusculas: ', len(texto), 'caracteres')


#d) rei por rainha
#print(texto.replace('rei','rainha'))


#E)
#print(texto.count('o'))






# 2 -
numeros = [10, 5, 8, 20, 15, 30, 25, 12]
#numeros.sort()
#a)
#print(numeros)


#B)
#numeros.sort(reverse=True)
#print(numeros)


#C)
#soma = sum(numeros)
#print(soma/len(numeros))


#D)
#print(max(numeros, key=int))


#E)
#print(min(numeros, key=int))




# 3 -
produtos = [("Camisa", 29.99), ("Calça", 59.99), ("Meia", 9.99), ("Tênis", 99.99), ("Boné", 19.99)]


#A)
# for nomes in produtos:
#     nomes += produtos[0]
#     print(nomes[0])


#B)


# for preco in produtos:
#    preco += produtos[0]
# print(preco[1])


#C)


# soma = 0
# for preco in produtos:
#    preco += produtos[0]
#    soma += preco[1]
# print(soma/len(produtos))


# D)


# maior = max(produtos)
# print(maior)






# 4 -
#A)
telefones = {"João": "1111-1111", "Maria": "2222-2222", "Pedro": "3333-3333", "Ana":
"4444-4444", "Lucas": "5555-5555"}
# nomes = telefones.keys()
# print(nomes)




#B)


# telefones = telefones.values()
# print(telefones)


#C)


# pedro = telefones['Pedro']
# print(pedro)




#D)


# telefones['Marcos'] = "7777-7777"
# print(telefones)




#E)
# telefones.pop('Ana')
# print(telefones)




# 5 -
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {4, 5, 6, 7, 8}




#A)


print(A.union(B))


#B)
print(B.intersection(C))


#C)
print(set(A) - set(B))


#D)
print(set(B) ^ set(C))


#E)
print(2 in set(A))


#F)
print(set(B) < set(C))
# 6 -


