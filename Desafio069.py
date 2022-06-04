# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


print('Sistema de cadastro v1')

maior = 0
homens = 0
mulheresMenor20 = 0

while True:
    print('=-=' *30)
    print('Cadastre uma pessoa: ')
    sexo = ' '
    cont = 0
    while sexo not in 'FfMm':
        sexo = str(input('Digite seu sexo [M/F]')).strip().upper()[0]
    idade = int(input('Digite sua Idade: '))
    if sexo in 'Mm':
        homens += 1
    if idade >= 18:
        maior += 1
    if sexo in 'Ff' and idade <= 20:
        mulheresMenor20 += 1
    print('=-='*30)
    computer = ' '
    while computer not in 'SsNn':
        computer = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if computer in 'Nn':
        print('=-=' * 30)
        break
print('Encerramos nosso programa com: ')
print(f'{homens} homens cadastrados, {mulheresMenor20} mulheres tendo menos de 20 anos e ', end='')
print(f'{maior} pessoas sendo maiores de idade!')