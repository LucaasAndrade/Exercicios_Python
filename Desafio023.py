# Faça um programa que leia um número de 0 à 9999 e mostre
# na tela cada um dos dígitos separados
# Exemplo: Digito 1834
# Unidade 4
# Dezena 3
# centena 8
# milhar 1

nu1 = str(input('Digite um número: '))
print('Esse número tem {} digítos. '.format(len(nu1)))
print('A Unidade desse número é {} '.format(nu1[-1]))
print('A Unidade de Dezena desse número é {} '.format(nu1[-2]))
print('A Unidade de Centena desse número é {} '.format(nu1[-3]))
print('A Unidade de Milhar desse número é {} '.format(nu1[-4]))
