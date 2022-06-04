# Escreva um programa que faça o computador "pensar " em um número inteiro
# Entre 1 e 5 e peça para o usuário tentar adivinhar qual foi o número
# Inventado pelo computador.
# O programa deverará escrever na tela se o usuari venceu ou perdeu.

from random import choice

pg = str(input('Vamos jogar um jogo? ')).lower()

if pg == 'sim':
    n1 = [1, 2, 3, 4, 5]
    sorteio = choice(n1)
    n2 = int(input('Escolha um número de 1 a 5: '))
    if n2 == sorteio:
        print('Parabéns você ganhou!!')
    else:
        print('Você não ganhou! O número certo era {}...'.format(sorteio))

else:
    print('Que pena, na próxima a gente joga...')
