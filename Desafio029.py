# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km excedido.

vl = int(input('Qual é a sua velocidade atual? '))

if vl <= 80:
    print('Você está no limite de velocidade, não será multado.')
else:
    multa = float(7.0)
    vl2 = (vl - 80) * multa
    print('Você foi multado! Deverá pagar uma multa no valor de R${:.2f}! '.format(vl2))
