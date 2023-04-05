# ======================================= MANIPULANDO TEXTO ===========================================

frase = 'ola mundo'
print(len(frase))   #Verifica a quantidade de caracteres.
print(frase.count('o'))  #Contar quantas vezes aparece O minusculo.
print(frase.find('mundo')) #Mostra em que posição começou 'mundo'. OBS: se colocar uma palavra que não possui na frase ele retorna o valor "-1".
print(frase.find('mundo1'))
print('mundo' in frase) # mostra se existe um valor dentro da frase.
print(frase.replace('ola', 'oi')) # vai substituir uma string por outra, neste caso 'ola' por 'oi'.
print(frase.upper()) # Escrever todas as frases em maiusculo.
print(frase.lower()) # Escrever todas as frases em minusculo. 
print(frase.capitalize()) # Transforma todas as primeiras letras de palavras em maiusculas.
print(frase.title()) # Escrever todas as frases em maiusculo.
print(frase.strip()) # Vai remover todos os espaços inuteis.
print(frase.rstrip()) # Vai remover os espaços inuteis somente da direita.
print(frase.lstrip()) # Vai remover os espaços inuteis somente da esquerda.
print(frase.split()) # Vai ocorrer uma divisão dentro da string considerando os espaços. transformando em uma lista.
print('-'.join(frase)) # Vai juntas as strings e colocar o '-'.
