print('=====','DESAFIO 018','======')

from math import sin, cos, tan, radians
angulo=int(input('Digite o angulo que voce deseja:'))

#####Conta para descobrir o SENO#####
seno=sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))

#####Conta para descobrir o COSENO#####
cosse=cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosse))

#####Conta para descobrir a TANGENTE#####
tan=tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tan))