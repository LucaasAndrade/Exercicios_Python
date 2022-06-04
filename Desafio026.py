# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes apearece A
# em que posição aparece pela primeira vez
# Em que posição aparece pela última vez

nome = str(input('Digite seu nome completo: ')).strip()
letra = str(input('Escolha uma letra: ')).strip()
print('A letra que você escolheu aparece {} vezes.'.format(nome.lower().count(letra)))
print('Ela apareceu primeiro na {} posição.'.format(nome.lower().find(letra)+1))
print('Apareceu pela última vez na {} posição.'.format(nome.lower().rfind(letra)+1))