print('=====','DESAFIO 020','=====')
####Embaralhando uma lista####
from random import shuffle
n1=str(input('Digite o nome do primeiro aluno:'))
n2=str(input('Digite o nome do segundo aluno:'))
n3=str(input('Digite o nome do terceiro aluno:'))
n4=str(input('Digite o nome do quarto aluno:'))
lista=[n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)