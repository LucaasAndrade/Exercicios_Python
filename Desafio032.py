# Faça um programa que leia um número qualquer e mstre se ele é Bissexto.

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é Bissexto! ')
else:
    print('Esse ano Não é Bissexto! ')
