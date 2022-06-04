# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e a tangente desse ângulo. 

import math

ang = float(input('Digite um ângulo qualquer: '))

rad = math.radians(ang)
cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)

print('O valor desse ângulo em radianos é {:.2f} '.format(rad))
print('O Seno desse ângulo é {:.2f}, \n O Cosseno desse ângulo é {:.2f} \n A Tângente desse ângulo é {:.2f}. '.format(sen, cos, tan))
