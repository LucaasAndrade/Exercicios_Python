# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o 
# menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


nm = int(input('Digite um número: '))
pergunta = str(input('Deseja continuar? [S|N] ').lower().strip()[0])
nm2 = nm
cont = 1
maior = 0
menor = nm

while pergunta == 's': 
    cont += 1
    nm = int(input('Digite outro número: '))
    nm2 += nm
    pergunta = str(input('Deseja continuar? [S|N] '))
    if nm >= maior:
        maior = nm
    elif nm <= nm:
        menor = nm
print(f'O programa encerrou com {cont} números mostrados.')
print(f'A média entre eles é de {nm2/cont}')
print(f'O maior valor mostrado foi {maior} e o menor {menor}.')