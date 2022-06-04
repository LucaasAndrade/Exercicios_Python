# Crie um programa que leia o nome de uma cidade e que diga se o nome dela
# E diga se o nome dela começa ou nao com o nome Santo

print('True = Sim e False = Não')
nome = str(input('Qual o nome da sua Cidade? '))
config = nome.lower().strip()
print('santo' in config)
