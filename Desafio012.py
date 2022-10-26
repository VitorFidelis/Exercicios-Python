print('=====','DESAFIO 012','=====')

produto=float(input('Digite o preço do produto: R$'))

##Calculo para saber o desconto em porcentagem##
desconto=produto*(5/100)
resultado=produto-desconto
#################################################

print(f'o novo preço do produto com o desconto de 5% é de:R${resultado:2.2f}')
