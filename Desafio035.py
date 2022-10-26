print('=====','DESAFIO 035','=====')
#########################################
print('\033[33m-=\033[m'*50)
print('\033[33m Analisandor de Triângulos \033[m')
print('\033[33m-=\033[m'*50)
#########################################
a=float(input('Primeiro segmento:'))
b=float(input('Segundo seguimento:'))
c=float(input('Terceiro segmento:'))
#########################################
if((a+b>c) and (a+c>b) and (c+b>a)):
    print('Os segmentos acima \033[32m PODEM FORMAR\033[m um triângulo!!')
else:
    print('Os segmentos acima \033[31m NÂO PODEM FORMAR\033[m um triângulo!!')