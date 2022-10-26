from traceback import print_list, print_tb


nome=str(input('Informe seu nome completo:')).strip()
#####Letras em maiuscolo#####
print('Seu nome em maiuscolo é: {}'.format(nome.upper()))
#####Letras em minuscuo#####
print('Seu nome em minusculo é: {}'.format(nome.lower()))
####Conta so as primeiras letras do nome#####
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
###Só conta as letras do priemiro nome####
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))