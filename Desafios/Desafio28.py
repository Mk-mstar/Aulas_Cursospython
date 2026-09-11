vel_carro = int(input('Digite a velocidade do seu carro (KM): '))
multa = vel_carro - 80 
multa_cal = multa * 7 
if vel_carro > 80: 
    print(f'Você foi multado por ultrapassar o limite de velocidade. Sua multa é: {multa_cal}')
else: 
    print('Você estava dentro do limite de velocidade.')