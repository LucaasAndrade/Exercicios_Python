# Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número de 0 à 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# forma necessários para vencer.

import random 

nmPc = random.randint(0, 10)
nmPlayer = int(input('Digite um número de 0 à 10: '))
tentativas = 1

while nmPlayer != nmPc:
    if nmPc < nmPlayer:
        print('Hmmmm, você digitou o número errado... tente diminuir o valor.')
    else:
        print('Hmmmm, você digitou o número errado... tente almentar o valor.')
    nmPlayer = int(input('Digite um número de 0 à 10: '))
    tentativas += 1
print(f'Você ganhou em {tentativas} tentativas!')
