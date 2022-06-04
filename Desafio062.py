#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
# alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

nm1 = int(input('Digite um valor: '))
nm2 = nm1
r = int(input('A razão da P.A: '))
cont = 0
mais = 10
total = 0
print(f'A P.A de {nm1} com razão {r} é : ', end='')
while mais != 0:
    total += mais 
    while cont <= total:
        cont += 1
        nm2 += r
        print(nm2, end='')
        print(' -> ', end='')
    print('Pause')
    mais = int(input('Quantos termos mais deseja ver? '))
print('FIM')
print(f'Foram mostrados {total} termos.')
