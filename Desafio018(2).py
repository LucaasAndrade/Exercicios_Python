# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e a tangente desse ângulo. 
import math

ang = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo {} tem o SENO de {:.2f} '.format(ang, seno))
coss = math.cos(math.radians(ang))
print(' O ângulo {} tem o COSSENO de {:.2f} '.format(ang, coss))
tan = math.tan(math.radians(ang))
print('O ângulo {} tem a Tângente de {:.2f} '.format(ang, tan))


