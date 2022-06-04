# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre suas médias.

nome = input('Nome do Aluno: ')
mt = input('Qual matéria quer registrar? ')
mt2 = input('Insira outra matéria: ')
n1 = float(input('Sua nota em {}: '.format(mt)))
n2 = float(input('Sua nota em {}: '.format(mt2)))
md = (n1 + n2) / 2
print('A nota de {} em {} foi {}, {} {} então sua média é {:.2f}'.format(
    nome, mt, n1, mt2, n2, md))
