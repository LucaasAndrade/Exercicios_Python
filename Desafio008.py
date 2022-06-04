# Desenvolva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros.

mt = float(input('Insira um valor em Metros: '))

print('{} metros é igual a: {} km, {} dm, {} cm, {} mm.'.format(
    mt, mt/(1000), mt*(10), mt*(100), mt*(1000)))
