#Nesse exercicio, foi pedido para digitarmos uma frase qualquer, encontrar quantas letras A tem nela,
#a primeira e a ultima vez que ela aparece na tela.
frase = input('Digite uma FRASE: ')
qvp = frase.count('a')
print(f'A quantidade de letra A é: {qvp}')
primeira = (frase.find('a'))
print(f'A primeira posição é: {primeira}')
ultima = (frase.rfind('a'))
print(f'A ultima posição é: {ultima}')