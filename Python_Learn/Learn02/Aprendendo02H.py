print('Essa Tinta pinta minha parede?')
a=float(input(('Digite a Altura da parede: ')))
l=float(input('Digite a Largura da parede:'))
t=int(input('Digite Quantos Metros Quadrados a tinta Gasta por Litro: '))
q=float(input('Digite Quantos Litros dessa Tinta você possui agora: '))
r=int(input('digite Quantas Mãos irá precisar: '))
p=a*l
m=p/t*r
tanque=m-q
total=q/m*100

print('Informações Totais: \n'
      'Area da Parede: {} metros Quadrados \n'
      'Rendimento da tinta por litro: {} metros quadrados \n'
      'Quantiedade Atual de Tinta: {} Litros \n'
      'Quantiedade de Repetições: {} \n'
      'Quantiedade de Tinta a ser Gasta: {} Litros \n'
      'Quanto Irá Precisar?: {} Litros \n'
      'Porcentagem de Tinta Atual necessaria: {} %'.format(p, t, q, r,m, tanque, total))