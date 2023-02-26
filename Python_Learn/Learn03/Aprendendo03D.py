import math

cop=float(input('Digite o Comprimento do Cateto Oposto: '))
cad=float(input('Digite o COmprimento do Cateto Adjasente: '))

hipo=math.hypot(cop, cad)
print('O Valor da Hipotenusa é {:.2f}'.format(hipo))
#hipo=cop**2+cad**2
#tenusa=math.sqrt(hipo)
#print('A Hipotenusa do Triangulo é {}.'.format(tenusa))
