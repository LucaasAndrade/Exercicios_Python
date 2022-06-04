# Escreva um programa que pergunte o salário de um funcionário e calcule o
# Valor de seu aumeto.
# Para salários superiores a R$1250.00 aumento de 10%.
# Para salários inferiores ou iguais aumento de 15%.

s1 = float(input('De quanto é o seu salário? R$ '))

if s1 >= 1250:
    print('O senhor(a) passará a receber R${:.2f}!'.format(((s1 * 10) / 100) + s1))

else:
    print('O senhor(a) passará a receber R${:.2f}!'.format(((s1 * 15) / 100) + s1))
