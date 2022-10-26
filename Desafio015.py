print('===== DESAFIO 015 =====')

dia=int(input('Quantos dias alugados?'))
km=float(input('Quantos de KM rodados?'))

#####Calculo de km e dias alugados##### 
total = (dia * 60) + (km * 0.15)
#######################################

print(f'O total a pagar é de R${total:.2f}')