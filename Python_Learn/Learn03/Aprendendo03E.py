import math
angulo=float(input('Digite o Valor do Angulo: '))
seno=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
print('O Angulo de {} tem o Seno de {:.2f} e o Cosseno de {:.2f}'.format(angulo, seno, cos))