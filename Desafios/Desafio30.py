km_viagem = float(input('Digite a quantidade em KM da sua viagem: '))
viagem1 = km_viagem * 0.50
viagem2 = km_viagem * 0.45
if km_viagem <= 200: 
    print(f'Sua viagem de {km_viagem} KM, deu R$ {viagem1}.')
else:
    print(f' Sua viagem de {km_viagem}KM, deu R$ {viagem2}')
