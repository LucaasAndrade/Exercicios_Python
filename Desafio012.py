# Faça um algoritimo que leia um preço de um produto e mostre seu nome preço, com 5% de desconto...

p1 = float(input('Qual o preço do produto? '))
p2 = float(input('Quanto de desconto a loja esta oferecendo? '))

calc = ((p1 * p2) / float(100)) - float(p1)
c2 = calc * float(-1)

print('O preço de um produto cujo preço é R${:.2f} com, {:.2f} por cento de desconto fica R${:.2f} . '.format(p1, p2, c2))
