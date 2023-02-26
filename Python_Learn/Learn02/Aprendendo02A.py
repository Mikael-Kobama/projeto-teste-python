#nome = str(input('Qual é o seu nome? '))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

x = int(input('Digite um Valor: '))
y = int(input('Outro Valor: '))
soma = x + y
multiplicacao = x * y
subtracacao = x - y
divisao = x / y
exponciacao = x ** y
divireal = x // y
resto = x % y
print('A soma vale {} '
      '\n) produto é {} \n'
      'e a divisão é {}'.format(soma, multiplicacao, divisao), end=' ')
print(' Divisão inteira {} e a potência {}'.format(divireal, exponciacao))
