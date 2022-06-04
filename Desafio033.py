# Faça um programa que leia três números e fala qual é o mior e qual é o menor.

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira o último número: '))

if n1 < n2 and n1 < n3:
    menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número é o {} '.format(maior))
print('O menor número é o {} '.format(menor))
