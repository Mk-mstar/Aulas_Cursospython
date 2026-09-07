
import json
import os

# Carrega os chamados existentes
if os.path.exists("chamados.json"):
    with open("chamados.json", "r", encoding="utf-8") as arquivo:
        chamados = json.load(arquivo)
else:
    chamados = []

print('==============SISTEMA HELP DESK==============')

print('Escolha uma das opções: \n 1 - Abrir chamado \n 2 - Ver chamados \n 3 - Pesquisar chamado \n 4 - Atualizar chamado \n 5 - Fechar chamado \n 6 - Relatório \n 0 - Sair ')

opcao = input('Escolha uma opção: ')

if opcao == "1":

    print('Abrindo chamado...')

    nome = input('Digite o seu nome: ')
    problema = input('Digite seu problema: ')
    prioridade = input('Digite a prioridade: \n 1 - Baixa \n 2 - Média \n 3 - Alta \n 4 - Crítica: \n ')

    chamado = {
        "nome": nome,
        "problema": problema,
        "prioridade": prioridade
    }

    chamados.append(chamado)

    with open("chamados.json", "w", encoding="utf-8") as arquivo:
        json.dump(chamados, arquivo, indent=4, ensure_ascii=False)

    print('Chamado registrado. Por favor, aguardar instruções.')

elif opcao == "2":

    print('Abrindo chamados registrados.')

elif opcao == "3":

    print('Pesquisando chamados.')

elif opcao == "4":

    print("Atualizando chamados.")

elif opcao == "5":

    print("Fechando chamado")

elif opcao == "6":

    print("Relatórios:")

elif opcao == "0":

    print('Saindo.')

