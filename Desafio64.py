# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles

nm = 0
cont = 0
soma = nm
nm = int(input('Digite um número qualquer: [999 para parar] '))

while nm != 999:
    cont += 1
    soma += nm
    nm = int(input('Digite um número qualquer: [999 para parar] '))  
print(f'Programa finalizado com {cont} números digitados!')
print(f'A soma dos números digitados é {soma}')