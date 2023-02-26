f=str(input('Digite o nome do funcionario: '))
s=float(input('Digite o salario atual: '))
a=int(input('Digite Quantos porcento terá de aumento: '))
c=s*a/100
aumento=s+c
print('O(A) Funcionario(a) {} Receberá um Aumento de {}%\n'
      'Sendo agora seu salario {:.2f} R$'.format(f,a,aumento))

