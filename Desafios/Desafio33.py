salario = float(input('Digite o valor do seu salário:'))
conta1 = salario * 0.10
conta2 = salario * 0.15
salario1 = salario + conta1
salario2 = salario + conta2
if salario >= 1250.00:
    print(f'O seu salário com reajuste de 10% ficou: {salario1}')
else: 
    print(f'O seu salário com reajuste de 15% ficou: {salario2}')