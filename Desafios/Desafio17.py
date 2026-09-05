import random
aluno = (input('Digite o nome do seu primeiro aluno.'))
aluno2 = (input('Digite o nome do seu segundo aluno.'))
aluno3 = (input('Digite o nome do seu terceiro aluno.'))
aluno4 = (input('Digite o nome do seu quarto aluno.'))

alunoescolhido = random.choice([aluno, aluno2, aluno3, aluno4])
print(f'O aluno escolhido para apagar a lousa foi: {alunoescolhido}')

