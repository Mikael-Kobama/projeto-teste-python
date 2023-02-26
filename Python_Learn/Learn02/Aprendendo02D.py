n=str(input('Digite O Nome do Aluno: '))
x1=float(input('Digite A Primeira Nota do Aluno: '))
while x1<0 or x1>10:
    x1=float(input('Digite a Nota Novamente: '))
x2=float(input('Digite A Segunda Nota do Aluno: '))
while x2<0 or x2>10:
    x2=float(input('Digite a Nota Novamente: '))
x3=float(input('Digite A Terceira Nota do Aluno: '))
while x3<0> x3>10:
    x3=float(input('Digite a Nota Novamente: '))
x4=float(input('Digite A Quarta Nota do Aluno: '))
while x4<0 or x4>10:
    x4=float(input('Digite a Nota Novamente: '))
m=(x1+x2+x3+x4)/4
while m<5.5:
    print(' A Média das Notas do(a) Aluno(a) {} é {:.2f} e está reprovado(a) '.format(n,m))
    break
while m>=5.5 and m<6:
    print(' A Média das Notas do(a) Aluno(a) {} é {:.2f} e pode recuperar '.format(n, m))
    break
while m>=6:
    print(' A Média das Notas do(a) Aluno(a) {} é {:.2f} e está Aprovadoo(a) '.format(n, m))
    break