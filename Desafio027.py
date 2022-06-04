# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
# Ex:
# primeiro: Ana
# Último: Solza

nome = str(input('Digite seu nome completo: ')).split(' ')
print('Seja Bem vindo! ')
print('Seu primeiro nome é {}.' .format(nome[0]))
print('Seu último nomr é {}'.format(nome[-1]))
