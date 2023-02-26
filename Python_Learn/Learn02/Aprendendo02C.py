x=int(input('Digite um valor: '))
while x<2:
    x=int(input('Digite um valor mais alto: '))
x1=x*2
x2=x*3
x3=x**(1/2)
print('Usando o número {}, temos:\n'
      'o Dobro do valor: {}\n'
      'o Triplo do valor: {}\n'
      'A Raiz quadrada: {:.2f}'.format(x, x1, x2, x3))
