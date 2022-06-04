# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos Dólares ela pode comprar
# Considere 1 US$ = R$ 3,27

n1 = float(input('Quanto dinheiro o(a) senhor(a) tem? R$'))
dl = n1 / float(3.27)

print('O(a) Senhor(a) tem R${} na Carteira então pode comprar US${:.2f} Dólares ' .format(n1, dl))
