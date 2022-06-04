num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print('Análisando o número {}...'.format(num))
print('A Unidade desse número é {} .'.format(u))
print('A Dezena desse número é {}.'.format(d))
print('A Cententena desse número é {}.'.format(c))
print('A Unidade de Milhar desse número é {}.'.format(um))
