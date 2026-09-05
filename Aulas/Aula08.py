#Comecamos a aula aprendendo import
#Exemplos: bebidas = cafe, leite, agua
#from import bebidas (ele ira importar todas as bebidas dentro da variável bebidas.)
#from bebidas import cafe (from faz com que consigamos importar apenas a bebida desejada.)
#Tivemos introducao as bibliotecas em python, por exemplo "Math"

import math
num = int(input('Digite um número:'))
r = math.sqrt (num)
print (f' A raiz quadrada de {num} é : {r:.2f}') 

#Acima tivemos uma introdução sobre alguns utilitarios da 
# biblioteca math, por exemplo sqrt que seria raiz quadrada
#  
import random
num = random.random()
print (f' O numero aleatorio é : {num} 🤑' )
#Acima tivemos uma introdução sobre a biblioteca random
