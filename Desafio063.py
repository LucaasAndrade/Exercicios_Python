# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os]
#  N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
# 1-1-2-3-5-8-13-21-34-55-89-144-233-377-610-987-1597--2584-4181-6765-10946 

valor = int(input('Quantos termos deseja ver? '))
vezes = valor 
cont = 0
nm1 = 0
nm2 = 1

print(f'0 - 1 - ', end='')
while cont <= valor:
    nm3 = nm1 + nm2
    print(f'{nm3} - ', end='')
    nm1 = nm2
    nm2 = nm3
    cont += 1
print('FIM')
