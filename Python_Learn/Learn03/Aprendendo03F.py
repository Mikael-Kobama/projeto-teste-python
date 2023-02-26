import random

alu1=str(input('Digite o Nome do Primeiro Aluno: '))
alu2=str(input('Digite o Nome do Segundo Aluno: '))
alu3=str(input('Digite o Nome do Terceiro Aluno: '))
alu4=str(input('Digite o Nome do Quarto Aluno: '))

lista_alunos=[alu1, alu2, alu3, alu4]

sorteio=random.choice(lista_alunos)
print('O aluno Escolhido pelo Sorteio é {}'.format(sorteio))