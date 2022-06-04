# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import randint

al1 = input('(Aluno 1) Qual o nome do primeiro aluno? ')
al2 = input('(Aluno 2) Qual o nome do segundo aluno? ')
al3 = input('(Aluno 3) Qual o nome do terceiro aluno? ')
al4 = input('(Aluno 4) Qual o nome do quinto aluno? ')

sortear = randint(1, 4)

print('O aluno que irá apagar o quadro será o Aluno {}... '.format(sortear))
