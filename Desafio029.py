print('=====','DESAFIO 029','=====')
##############################################################################
velocidade=float(input('Qual a velocidade atual do carro?'))
##############################################################################
if(velocidade > 80):
    print('Você ultrapassou a velocidade permitida de 80Km/h')
    print('a multa será no valor de:R${:.2f}'.format((velocidade-80) * 7))
else:
    print('Você não ultrapassou a velocidade permitida.')
    print('Tenha um bom dia!! Dirija sempre com segurança!')