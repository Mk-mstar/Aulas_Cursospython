print ('BEM VINDO A ESCOLA MAIS DIFICIL DO BRASIL!')
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2
print(f'Sua média é: {m:.2f}')
if m >= 8.0: 
    print('Parabéns, você passou!')
else:
    print('Opa, você reprovou! ;( ')