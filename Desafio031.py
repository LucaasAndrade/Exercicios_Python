# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem cobrando R$0.50 para viagens abaixo de 200km
# E R$0.45 para viagens longas

ps = int(input('Qual é a distância da sua viagem? '))
if ps >= 200:
    print('O senhor irá pagar R${} na sua passagem! '.format(ps * 0.50))
else:
    print('O senhor irá pagar R${} na sua passagem! '.format(ps * 0.45))
