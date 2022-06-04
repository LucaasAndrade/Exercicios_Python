# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

nm1 = int(input('Insira um valor: '))
cont = 0
calc = 1

while cont != nm1:
    cont += 1
    calc = cont * calc
print(f'O valor que você digitou foi {nm1}' )
print(f'{nm1}! = {calc}')