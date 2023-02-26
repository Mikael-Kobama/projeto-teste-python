
a=float(input('Digite o valor de a: '))
b=float(input('Digite o Valor de b: '))
c=float(input('Digite o valor de c: '))
delta=(b**2)-4*a*c
if delta<0:
    print('Não há raizes reais. Digite Os valores Novamente')
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o Valor de b: '))
    c = float(input('Digite o valor de c: '))
raizdedelta=delta**(1/2)
x1=(-b+raizdedelta)/2*a
if delta>0:
    x2=(-b-raizdedelta)/2*a
    print('x = {}'.format(x1))
    print('x = {}'.format(x2))
else:
    x1=(-b+raizdedelta/(2*a))
    x2=(-b+raizdedelta/(2*a))

    print('x1 é igual a {:.2f} e x2 é igual a {:.2f}'.format(x1,x2))

