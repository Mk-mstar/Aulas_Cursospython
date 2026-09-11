reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Parabéns, você formou um triangulo.')
else: 
    print('Você não formou um triangulo.')