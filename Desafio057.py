# Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'.
# Caso esteja errado, peça digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: [F/M] ').strip()).upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [F/M] ').strip()).upper()[0]
print(f'[{sexo}] Seu sexo foi registrado com sucesso!')