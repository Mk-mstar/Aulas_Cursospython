import random
num_pc = [0,1,2,3,4,5]
num_escolhido = random.choice(num_pc)

num_user = int(input('Digite um número aleátorio de 0 a 5: '))
if num_user == num_escolhido:
    print(f'Parabéns! o número escolhido pelo PC foi: {num_escolhido}!')
else:
    print(f'Errou! tente novamente, o número escolhido pelo PC foi: {num_escolhido}')