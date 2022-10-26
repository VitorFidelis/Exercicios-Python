print('=====','DESAFIO 031','=====')

km=int(input('Qual a distancia da sua viagem ?'))
##############################################################################
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(km))
##############################################################################
if(km <= 200):
    print('O preço a pagar sera de:R${:.2f}'.format(km * 0.50))
else:
    print('O preço a pagar é de:R${:.2f}'.format(km * 0.45))