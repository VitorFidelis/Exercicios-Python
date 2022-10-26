from random import choice
#### Sorteando alunos informado #####
a1=str(input('Digite o nome do primeiro aluno:'))
a2=str(input('Digite o nome do segundo aluno:'))
a3=str(input('Digite o nome do terceiro aulo:'))
a4=str(input('Digite o nome do quarto aluno:'))
lista=[a1,a2,a3,a4]
print('O aluno escolido foi:{}'.format(choice(lista)))