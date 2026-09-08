#Faca um programa que leia o nome completo
#de uma pessoa, mostrando em seguida o
#primeiro e o ultimo nome separadamente

nome = input('Digite seu nome: ')
nome_separado = nome.split()

primeiro = nome_separado[0]
print(f'O primeiro nome é: {primeiro}')

ultimo = nome_separado[-1]
print(f'O último nome é: {ultimo}')