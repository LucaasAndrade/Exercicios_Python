# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# Se elas podem ou  não formar um triângulo

r1 = float(input('Qual é a medida da primeira reta? '))
r2 = float(input('Qual é a medida da segunda reta? '))
r3 = float(input('Qual é a medida da terceira reta? '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As Retas formam um Triângulo! ')

else:
    print('As Retas não formam um Triângulo! ')