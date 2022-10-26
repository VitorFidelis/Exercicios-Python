from random import randint
from time import sleep
##########################################################################
numero=randint(0, 5)#Faz o copuutadador sortear um número
##########################################################################
print('-=-'*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*50)
##########################################################################
resposta=int(input('Em que número eu pensei??: '))#Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
##########################################################################
if(resposta==numero):
    print('Você acertou!! Parabéns ganhador, consegiu me vencer dessa vez!!')
else:
    print('Ganhei!! Eu pensei no número {} e não no {}'.format(numero,resposta))