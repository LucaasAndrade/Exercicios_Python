# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
computador = int(input('digite o valor de saque: R$ '))
while True:
    if computador >= 50:
        nota50 += 1
        computador -= 50
    elif computador >= 20:
        nota20 += 1
        computador -= 20
    elif computador >= 10:
        nota10 += 1
        computador -= 10
    else:
        nota1 += 1
        computador -= 1
    if computador == 0:
        break

print(f'Você sacou R${computador} e recebeu {nota50} notas de R$50; {nota20} notas de R$20; ')
print(f'{nota10} Notas de R$10 e {nota1} notas de R$1')