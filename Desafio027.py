print('=====','DESAFIO 027','=====')

n=str(input('Digte o seu nome completo:')).strip()
nome=n.split()
print('O seu primeiro nome é:{}'.format(nome[0]))
print('O seu ultimo nome é:{}'.format(nome[len(nome)-1]))