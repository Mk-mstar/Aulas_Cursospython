import math
co = int(input('Digite o comprimento do cateto oposto'))
ca = int(input('Digite o comprimento do cateto adjacente'))

rco = math.pow(co, 2)
rca = math.pow(ca, 2)
scat = rco + rca
rscat = math.sqrt(scat)

print(f'A hipotenusa mede {rscat:.2f}')