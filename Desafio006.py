# Crie um algoritmo que leia um número e mostre seu dobro, triplo e sua raiz quadrada

n1 = float(input('Escolha um número: '))
d = n1 * float(2)
t = n1 * float(3)
rq = n1 ** float(1/2)

print('O dobro de {} é {}, o triplo {} e sua raiz quadrada é {:.3f} .'.format(n1, d, t, rq))