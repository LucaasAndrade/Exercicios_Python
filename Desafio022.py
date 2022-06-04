# crie um programa que leia o nome de uma pessoa e mostre;
# O nome com todas letras maiusculas;
# O nome com todas letras minusculas
# quantas letras ao todo(sem considerar espaços);
# Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome em letras Maiúsculas ficaria: {} '.format(nome.upper()))
print('Seu nome em letras Minúsculas ficaria: {} '.format(nome.lower()))
print('Seu nome ao todo tem {} carecteres. '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} carectares. '.format(nome.find(' ')))
