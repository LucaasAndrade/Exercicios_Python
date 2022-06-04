# Escreva um programa que pergunte  a quantidade de Km percorridos por um carro alugado e aquantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sebendo que o carro custa R$60 por dia e R$0,15 pir Km rodado.

v1 = int(input('Quantos dias ficou com o Veicúlo? '))
v2 = float(input('Quantos Km rodou com o Veicúlo? '))

calc = (v1 * 60) + (v2 * 0.15)

print('O total a pagar é de: R${}'.format(calc))
