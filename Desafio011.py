# Faça um Programa que leia a Largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta que será usada sabendo que cada litro de tinta pinta uma área de 2m2.

l = float(input('Qual é a largura da parede? '))
a = float(input('Qual é a altura da perede? '))
area = l * a
qt = area / float(2)

print('A quantidade de tinta que será usada para pintar uma parede cuja área mede {}m2, será de {:.2f} litros.'.format(area, qt))
