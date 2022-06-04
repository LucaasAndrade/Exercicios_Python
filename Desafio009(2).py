# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada

n1 = int(input('Escolha um número: '))
a = n1 * int(1)
b = n1 * int(2)
c = n1 * int(3)
d = n1 * int(4)
e = n1 * int(5)
f = n1 * int(6)
g = n1 * int(7)
h = n1 * int(8)
i = n1 * int(9)
j = n1 * int(10)

print('Tabuada do {} '.format(n1))
print(' | 1 x {} = {} | \n | 2 x {} = {} | \n | 3 x {} = {} | \n | 4 x {} = {} | \n | 5 x {} = {} | \n | 6 x {} = {} | \n | 7 x {} = {} | \n | 8 x {} = {} | \n | 9 x {} = {} | \n | 10 x {} = {} |  '.format(
    n1, a, n1, b, n1, c, n1, d, n1, e, n1, f, n1, g, n1, h, n1, i, n1, j))
