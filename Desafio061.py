# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

nm1 = int(input('Digite um valor: '))
nm2 = nm1
r = int(input('A razão da P.A: '))
cont = 0

print(f'A P.A de {nm1} com razão {r} é : ', end='')
while cont != 10:
    cont += 1
    nm2 += r
    print(nm2, end='')
    print(', ' if cont < 10 else ' ... ', end='')
print(f'\nEsses foram os primeiros 10 termos da P.A {nm1} com razão {r} ')
