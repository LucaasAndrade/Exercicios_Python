# Faça um programa que leia um numero inteiro e mostre seu sucessor e seu antecessor

n1 = int(input('Escolha um número: '))
a = n1 - int(1)
s = n1 + int(1)
print('O antecessor de {} é {} e o seu secessor é {}'.format(n1, a, s))