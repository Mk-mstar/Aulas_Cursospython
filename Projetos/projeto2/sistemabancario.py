import os
import json

criador_user = ''
criador_senha = ''
saldo = 0.0

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo_json = os.path.join(pasta, 'user.json')

if not os.path.exists(arquivo_json):
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump({}, arquivo)

print("""BEM VINDO AO BANCO DO KAKÁ
VOCÊ DESEJA: 
1. CRIAR CONTA
2. FAZER LOGIN
3. DEPOSITAR
4. SACAR""")

opcao = input('Escolha uma opção: ')

if opcao == "1":
    print('BEM VINDO AO CRIADOR DE CONTAS')

    criador_user = input('Crie seu nome de usuario: ')
    criador_senha = input('Crie sua senha: ')

    conta = {
        "usuario": criador_user,
        "senha": criador_senha,
        "saldo": 0.0
    }

    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(conta, arquivo, indent=4)

    print('Usuário criado, vá agora para o sistema de login')

elif opcao == "2":
    print('BEM VINDO AO SISTEMA DE LOGIN')

    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        conta = json.load(arquivo)

    if 'usuario' not in conta:
        print('Nenhuma conta cadastrada!')
    else:
        user = input('Digite seu nome de usuario: ')
        senha = input('Digite sua senha: ')

        if user == conta['usuario'] and senha == conta['senha']:
            print('Usuário encontrado.')
        else:
            print('Usuário ou senha incorretos.')

elif opcao == "3":
    print('SISTEMA DE DEPÓSITO')
    
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        conta = json.load(arquivo)
    
    if 'saldo' not in conta:
        print('Erro: Nenhuma conta ativa encontrada para depositar.')
    else:
        saldo_atual = float(conta['saldo'])
        saldo_novo = float(input('Digite a quantia que você quer depositar: '))
        
        saldo_reajustado = saldo_atual + saldo_novo
        
        conta['saldo'] = saldo_reajustado
        with open(arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(conta, arquivo, indent=4)
            
        print(f'O saldo reajustado ficou em: R$ {saldo_reajustado:.2f}')

elif opcao == "4":
    print('SISTEMA DE SAQUE')
    
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        conta = json.load(arquivo)
        
    if 'saldo' not in conta:
        print('Erro: Nenhuma conta ativa encontrada para sacar.')
    else:
        saldo_atual = float(conta['saldo'])
        saldo_saque = float(input('Digite a quantia que você deseja sacar: '))
        
        if saldo_saque > saldo_atual:
            print('Saldo insuficiente para realizar o saque!')
        else:
            saldo_reajustado = saldo_atual - saldo_saque
            
            conta['saldo'] = saldo_reajustado
            with open(arquivo_json, "w", encoding="utf-8") as arquivo:
                json.dump(conta, arquivo, indent=4)
                
            print(f'Saque realizado com sucesso!')
            print(f'O saldo reajustado ficou em: R$ {saldo_reajustado:.2f}')
else:
    print('Opção inválida!')
