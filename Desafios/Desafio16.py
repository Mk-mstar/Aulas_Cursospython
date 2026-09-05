import math

ang = int(input('Digite um angulo qualquer'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O valor do seu angulo é {ang}, o seno é {sen:.2f} , o cosseno é {cos:.2f} e o tangente é {tan:.2f}')