print("====","DESAFIO 033","=====")

n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
n3=int(input('Terceiro valor:'))

#Verificando quem é o menor
menor=n1 
if((n2<n1) and (n2<n3)):
    menor=n2
if((n3<n2) and(n3<n1)):
    menor=n3
#Verificando quem é o maior
maior=n1
if((n2>n1) and (n2>n3)):
    maior=n2
if((n3>n2) and (n3>n1)):
    maior=n3

print('O maior número é:{}'.format(menor))
print('O maior núemro é:{}'.format(maior))