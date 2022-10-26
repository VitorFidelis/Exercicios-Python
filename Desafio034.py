print('=====','DESAFIO 034','=====')
##################################
salario=float(input('Qual é o salário do funcionário?'))
#################################
if(salario<=1250):
    novo= salario+(salario*15)/100
else:
    novo=salario+(salario*10)/100
#################################
print('O salário de quem ganhava:\033[31mR${:.2f}\033[m'.format(salario))
print('Agora passara a ser:\033[32mR${:.2f}\033[m'.format(novo))