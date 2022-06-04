# Crie um programa que leia dois números e mostre como o menu ao lado da Tela.
# Seu programa deverá realizar a operação solicitada [1] Somar [2] Multiplicar [3] Maior
# [4] Novos números [5] sair

nm1 = int(input('Digite um número: '))
nm2 = int(input('Digite outro número: '))
painel = 0

while painel != 5:
    print(
"""
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
""")
    usuario = int(input('Escolha a opção que deseja seguir: '))
    painel = usuario
    if usuario ==  1: 
        print(f'{nm1} Somado à {nm2} resulta em {nm1 + nm2}')
    elif usuario == 2:
        print(f'{nm1} X {nm2} = {nm1 * nm2}')
    elif usuario == 3:
        if nm1 < nm2:
            print(f'{nm1} & {nm2}. O maior número é {nm2}')
        else:
            print(f'{nm1} & {nm2}. O maior númeor é {nm1}')
    elif usuario == 4:
        nm1 = int(input('Digite um núemro: '))
        nm2 = int(input('Digite outro número: '))
    elif usuario >= 6:
        print('Opção inválida, tente novamente!')   
print('Fim do programa! Obrigado por me escolher <3')