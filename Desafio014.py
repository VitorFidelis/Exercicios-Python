print('==== DESAFIO 014 ====')

celsius=float(input('Informe a temperatura em °C:'))
fahre=float(input('Informe a temperatura em °F:'))

######### Calculo de celsius para fahrenheit ########
fare = 32 + (celsius * 1.8) 
#####################################################

######### Calculo de fahrenheit para celsius ########
cesl= (fahre - 32)/1.8
######################################################
print('A temperatura em {} °C corresponde {} °F.'.format(celsius,fare))

print('A temperatura em {} °F corresponde {:.2f} °C.'.format(fahre,cesl))