import json
import os

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(pasta, "chamados.json")

if os.path.exists(arquivo_json):
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        try:
            chamados = json.load(arquivo)
        except json.JSONDecodeError:
            chamados = []
else:
    chamados = []

print('============== SISTEMA HELP DESK ==============')

print('''Escolha uma das opções:

1 - Abrir chamado
2 - Ver chamados
3 - Pesquisar chamado
4 - Atualizar chamado
5 - Fechar chamado
6 - Relatório
0 - Sair
''')

opcao = input('Escolha uma opção: ')


if opcao == "1":

    print('Abrindo chamado...')

    nome = input('Digite o seu nome: ')
    problema = input('Digite seu problema: ')
    prioridade = input(
        'Digite a prioridade: \n'
        '1 - Baixa \n'
        '2 - Média \n'
        '3 - Alta \n'
        '4 - Crítica: \n'
    )

    novo_id = len(chamados) + 1

    chamado = {
        "id": novo_id,
        "nome": nome,
        "problema": problema,
        "prioridade": prioridade,
        "status": "Aberto"
    }

    chamados.append(chamado)

    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(chamados, arquivo, indent=4, ensure_ascii=False)

    print('Chamado registrado. Por favor, aguardar instruções.')



elif opcao == "2":

    print('Abrindo chamados registrados.')

    if len(chamados) == 0:
        print('Nenhum chamado registrado.')

    else:
        for chamado in chamados:
            print(f"Chamado #{chamado['id']}")
            print(f"Nome: {chamado['nome']}")
            print(f"Problema: {chamado['problema']}")
            print(f"Status: {chamado['status']}")
            print("-" * 30)

elif opcao == "3":

    print('Pesquisando chamados...')

    pesquisa = input('Digite o numero do chamado: ')
    encontrado = False

    for chamado in chamados:

        if str(chamado['id']) == pesquisa:

            print(f"Chamado #{chamado['id']}")
            print(f"Nome: {chamado['nome']}")
            print(f"Problema: {chamado['problema']}")
            print(f"Status: {chamado['status']}")

            encontrado = True
            break

    if not encontrado:
        print('Id não encontrado.')



elif opcao == "4":

    numero = input('Digite o Id do chamado: ')
    encontrado = False

    for chamado in chamados:

        if str(chamado['id']) == numero:

            encontrado = True

            novo_status = input("""Escolha o novo status:

1 - Aberto
2 - Em andamento
3 - Aguardando usuário
4 - Resolvido

Escolha: """)

            if novo_status == "1":
                chamado['status'] = 'Aberto'

            elif novo_status == "2":
                chamado['status'] = 'Em andamento'

            elif novo_status == "3":
                chamado['status'] = 'Aguardando usuário'

            elif novo_status == "4":
                chamado['status'] = 'Resolvido'

            else:
                print("Status inválido.")
                break

            with open(arquivo_json, "w", encoding="utf-8") as arquivo:
                json.dump(chamados, arquivo, indent=4, ensure_ascii=False)

            print("Chamado atualizado com sucesso!")
            break

    if not encontrado:
        print("Chamado não encontrado.")



elif opcao == "5":

    numero = input('Digite o id do chamado que você quer fechar: ')
    encontrado = False

    for chamado in chamados:

        if str(chamado['id']) == numero:

            chamado['status'] = "Fechado"
            encontrado = True

            with open(arquivo_json, "w", encoding="utf-8") as arquivo:
                json.dump(chamados, arquivo, indent=4, ensure_ascii=False)

            print("Chamado fechado com sucesso!")
            break

    if not encontrado:
        print("Chamado não encontrado.")


elif opcao == "6":

    print("Relatórios:")

    total = len(chamados)
    abertos = 0
    andamento = 0
    resolvidos = 0
    fechados = 0

    for chamado in chamados:

        if chamado['status'] == "Aberto":
            abertos += 1

        elif chamado['status'] == "Em andamento":
            andamento += 1

        elif chamado['status'] == "Aguardando usuário":
            pass

        elif chamado['status'] == "Resolvido":
            resolvidos += 1

        elif chamado['status'] == "Fechado":
            fechados += 1

    print(f'O número total de chamados é {total}')
    print(f'O número de chamados em aberto é {abertos}')
    print(f'O número de chamados em andamento é {andamento}')
    print(f'O número de chamados resolvidos é {resolvidos}')
    print(f'O número de chamados fechados é {fechados}')



elif opcao == "0":

    print('Saindo.')