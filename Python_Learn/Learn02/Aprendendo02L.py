modelo=str(input('Digite O modelo do Carro: '))
km=float(input(('Digite Quantos Km foram rodados: ')))
d=int(input('Digite Quantos Dias  ele foi alugado: '))

t=km*0.15+60*d
print('='*22)
print('Carro: {} \n'
      'Dias Alugados: {} \n'
      'Km Rodados: {} \n'
      'Total a Pagar: {:.2f}'.format(modelo,d,km,t))
print('='*22)