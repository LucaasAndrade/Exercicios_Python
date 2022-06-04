# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, ]
# para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    nm = int(input('Insira um valor: '))
    if nm <= 0:
        break
    for mult in range(0, 11):
        print(f'{nm} X {mult} = {nm*mult}')
print('O programa foi encerrado.')