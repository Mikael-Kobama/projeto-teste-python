print('==Tabelando Preços==')
p=str(input('Digite Qual Produto: '))
v=float(input('Digite Qual Valor Atual: '))
d=int(input('Digite Quanto de Desconto Terá: '))

c=v*d/100
l=v-c
print('Produto: {:=^4}\n'
      'Preço antigo: {:=^2} R$\n'
      'Preço atual: {:=^3} R$'.format(p,v,l))
