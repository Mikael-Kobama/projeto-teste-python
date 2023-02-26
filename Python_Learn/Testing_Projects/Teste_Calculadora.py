from math import factorial
print('=============Bem-Vindo=============')
print('A Calculadora possui essas opções: \n'
      'Soma = Digite soma \n'
      'Multiplicação = Digite multiplica \n'
      'Divisão = Digite divide \n'
      'Raiz Quadrada = Digite raiz \n'
      'Fatorial = Digite fator')
calcu=str(input('Digite Qual Operação: '))
if calcu=='soma':
    calcu=float(input('Primeiro Numero: '))
    soma2=float(input('Segundo Numero: '))
    soma=calcu+soma2
    print('Resultado é {}'.format(soma))
elif calcu=='multiplica':
    x1=float(input('Primeiro Numero: '))
    x2=float(input('Segundo Numero: '))
    multiplica=x1*x2
    print('O Resultado é {}'.format(multiplica))
elif calcu=='divide':
    d1=float(input('Primeiro Numero: '))
    d2=float(input('Segundo Numero: '))
    divide=d1/d2
    print('O Resultado é {}'.format(divide))
elif calcu=='raiz':
    r=float(input('Numero: '))
    raiz=r**(1/2)
    print('A raiz quadrada é {}'.format(raiz))
elif calcu=='fator':
    f=int(input('Qual Numero: '))
    fator=factorial(f)
    print('O Fatorial do numero é {}'.format(fator))
print('==============Obrigado==============')

