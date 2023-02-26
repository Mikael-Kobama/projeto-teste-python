import math
r=int(input('Coloque o valor do raio da circuferencia: '))
while r>1000:
    r=int(input('Valor muito alto. coloque um valor menor:'))
else:
    d=2*r
    diametro=d
    round(diametro, 2)
    p=2*r*math.pi
    perimetro=p
    round(perimetro, 2)
print('Utilizando o raio {}, você obterar o diametro da Circurefencia: {:.2f}. '
      '\nE o Perimeto da Circuferencia: {:.2f} '.format(r, diametro,
                                                         perimetro))