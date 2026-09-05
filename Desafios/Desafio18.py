import random
aluno = "C"
aluno2 = "d"
aluno3 = "a"
aluno4 = "B"

lista_alunos = [aluno, aluno2, aluno3, aluno4]
ordem_alunos = random.sample(lista_alunos, len(lista_alunos))
print(f'A ordem dos alunos sorteada foi: {ordem_alunos}')