# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
menorrProduto = ''
maior1000 = 0
memoria = 10000

while True:
    nomeProduto = str(input('Informe o nome do produto: ')).strip().capitalize()
    precoPorduto = float(input('Informe o preço: R$  '))
    total += precoPorduto
    if precoPorduto < memoria:
        menorProduto = nomeProduto 
        memoria = precoPorduto
    if precoPorduto >= 1000:
        maior1000 += 1
    computador = ' '
    while computador not in 'SsNn':
        computador = str(input('Deseja cadastrar mais algum produto? [S/N]')).strip().upper()[0]
    if computador in 'Nn':
        break
    print('=-='*30)
print('Programa Finalizado!')
print(f'Total {total:3,}')
print(f'{maior1000} produtos custaram mais de R$1000,00')
print(f'{menorProduto} foi o produto mais barato!')
