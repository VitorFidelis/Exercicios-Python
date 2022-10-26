print('=====','DESAFIO 004','=====')

n=input('Digite algo:')
print('O tipo primitivo desse valor é:',type(n))
print('É alfanúmerico?',n.isalnum())
print('É alfabetico?',n.isalpha())
print('É minúsculas?',n.islower())
print('É um número?',n.isnumeric())
print('É maiúsculas',n.isupper())
print('É somente espaços?',n.isspace())
print('É capitalizado?',n.istitle())

print('*'*50)
#testando com comedo formatado
print(f'E NUMERO:{n.isnumeric()}')
print('E NUMERO:{}'.format(n.isalpha()))