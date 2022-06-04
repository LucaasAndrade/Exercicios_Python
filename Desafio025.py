# Crie um programa que leia o nome de uma pessoa e diga se ela
# tem ou não Silva no nome
print('True = Sim False = Não')
nome = str(input('Qual é o seu nome completo: ')).strip()
print('silva' in nome.lower())
