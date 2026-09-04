 # + "Adição"
 # - "Subtração"
 # / "Divisão"
 # * "Multiplicação"
 # ** "Potencia"
 # // "Divisão inteira"
 # % "Resto da divisão"

n1 = int(input('Digite um valor'))
n2 = int(input('Digite um valor'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 

print(f'A soma é {s}, o produto é {m}, e a divisão é {d:.3f}', end='')
print(f'A divisão inteira é {di}, e potencia é {e}')