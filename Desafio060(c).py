# Fatorial com laços de repetição controladas 

nm1 = int(input('Digite um número: '))
mult = 1
print(f'{nm1}!= ', end=' ')
for c in range(nm1, 0, -1):
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    mult *= c
print(f' {mult}')

