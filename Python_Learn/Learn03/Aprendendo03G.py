import random

alu1=str(input('Primeiro Aluno: '))
alu2=str(input('Segundo Aluno: '))
alu3=str(input('Terceiro Aluno: '))
alu4=str(input('Quarto Aluno: '))
ordem=[alu1, alu2, alu3, alu4]
random.shuffle(ordem)
#ordem2=tuple(ordem)
#ran=random.sample(ordem2, k=4)
print('A ordem dos Alunos a apresentar é: \n'
      '{}'.format(ordem))
