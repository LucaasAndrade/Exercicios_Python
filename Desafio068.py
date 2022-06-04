# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

import random
from time import sleep

cont = 0
vitorias = 0

print('\033[031m=-=\033[m'* 30 )
print('SEJAM BEM VINDOS AO PAR OU IMPAR')
print('\033[031m=-=\033[m'* 30 )

while True:
    question_Game = str(input('Escolhar Par ou Ímpar: [P/I] ')).strip().upper()[0]
    print('\033[031m=-=\033[m'* 30 )
    if question_Game not in 'PpIi':
        print('Não entendi. Tente Novamente!')
        print('\033[031m=-=\033[m'* 30 )
    else:
        cont += 1
        number_player = int(input('Jogue um número de 0 à 9: '))
        print('\033[031m=-=\033[m'* 30 )
        computer = random.randint(0, 9)
        sleep(1)
        print('PAR')
        sleep(1)
        print('OU')
        sleep(1)
        print('IMPAR!')
        sleep(0.5)
        print('\033[031m=-=\033[m'* 30 )
        if question_Game in 'Pp':
            if (number_player + computer) % 2 == 0:
                print('Droga! Você ganhou....')
                print('\033[031m=-=\033[m'* 30 )
                print(f'{computer} + {number_player} = {computer+number_player}')
                print('\033[031m=-=\033[m'* 30 )
                print('Vamos mais uma!')
                print('\033[031m=-=\033[m'* 30 )
                vitorias += 1
            else:
                print('HA! Você Perdeu! ')
                print('\033[031m=-=\033[m'* 30 )
                print(f'{computer} + {number_player} = {computer+number_player}')
                print('\033[031m=-=\033[m'* 30 )
                break
        if question_Game in 'Ii':
            if (number_player + computer) % 2 != 0:
                print('Droga! Você ganhou....')
                print('\033[031m=-=\033[m'* 30 )
                print(f'{computer} + {number_player} = {computer+number_player}')
                print('\033[031m=-=\033[m'* 30 )
                print('Vamos mais uma!')
                print('\033[031m=-=\033[m'* 30 )
                vitorias += 1
            else:
                print('HA! Você Perdeu!')
                print('\033[031m=-=\033[m'* 30 )
                print(f'{computer} + {number_player} = {computer+number_player}')
                print('\033[031m=-=\033[m'* 30 )
                break

print('O jogo acabou!')
print(f'Você ganhou {vitorias} vezes!')
print('\033[031m=-=\033[m'* 30 )


print('Developed by Andrade2k22៹')