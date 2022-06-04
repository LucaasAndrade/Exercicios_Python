# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo sálario, com 15% de aumento.

n = input('Qual é o nome do funcionário? ')
s1 = float(input('Qual é o sálario atual de {} ?'.format(n)))
s2 = float(input('Qual o percentual de aumento ? '))

c = ((s1 * s2) / 100) + s1

print('O sálario de {} após o aumento será de R${:.2f} .'.format(n, c))
