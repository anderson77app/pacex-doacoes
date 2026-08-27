# SISTEMA SOLIDÁRIO DE GESTÃO DE DOAÇÕES

estoque_doacoes = {}

def cadastrar_doacao():
    item = input("Digite o nome do item para doação (ex: Arroz, Roupas): ").strip().upper()
    try:
        quantidade = int(input(f"Digite a quantidade de '{item}': "))
        if item in estoque_doacoes:
            estoque_doacoes[item] += quantidade
        else:
            estoque_doacoes[item] = quantidade
        print(f"\n[SUCESSO] {quantidade} unidade(s) de '{item}' adicionada(s)!")
    except ValueError:
        print("\n[ERRO] Por favor, digite apenas números para a quantidade.")

def listar_doacoes():
    print("\n--- ESTOQUE ATUAL DE DOAÇÕES ---")
    if not estoque_doacoes:
        print("O estoque está vazio no momento.")
    else:
        for item, quantidade in estoque_doacoes.items():
            print(f"- {item}: {quantidade} unidade(s)")
    print("--------------------------------")

def retirar_doacao():
    item = input("Digite o nome do item que deseja retirar: ").strip().upper()
    if item in estoque_doacoes:
        try:
            qtd_retirar = int(input(f"Temos {estoque_doacoes[item]} de '{item}'. Quantas deseja retirar? "))
            if qtd_retirar <= estoque_doacoes[item]:
                estoque_doacoes[item] -= qtd_retirar
                print(f"\n[SUCESSO] Retirada confirmada. Restam {estoque_doacoes[item]} de '{item}'.")
                if estoque_doacoes[item] == 0:
                    del estoque_doacoes[item] # Remove o item do estoque se zerar
            else:
                print("\n[ERRO] A quantidade pedida é maior que a disponível no estoque.")
        except ValueError:
            print("\n[ERRO] Por favor, digite um número válido.")
    else:
        print("\n[ERRO] Item não encontrado no estoque.")

# Loop do Menu Principal
while True:
    print("\n=== SISTEMA DE GESTÃO DE DOAÇÕES ===")
    print("1. Cadastrar nova doação")
    print("2. Listar doações no estoque")
    print("3. Retirar doação (Entrega a famílias)")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    if opcao == '1':
        cadastrar_doacao()
    elif opcao == '2':
        listar_doacoes()
    elif opcao == '3':
        retirar_doacao()
    elif opcao == '4':
        print("\nEncerrando o sistema. Obrigado pelo seu trabalho voluntário!")
        break
    else:
        print("\n[ERRO] Opção inválida. Escolha um número de 1 a 4.")
