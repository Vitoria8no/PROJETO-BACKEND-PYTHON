from banco import criar_tabela, adicionar_usuario, listar_usuarios,deletar_usuario,atualizar_email,buscar_usuario,exportar_dados
import os
# Prepara o banco assim que o programa abre
criar_tabela()

while True:
    os.system('cls')
    print("\n--- SISTEMA MODULAR ---")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. atualizar")
    print("4. deletar")
    print("5. Sair")
    print("6. exportar")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        n = input("Nome: ")
        e = input("Email: ")
        adicionar_usuario(n, e)
        print("✅ Sucesso!")
        
    elif opcao == "2":
        usuarios = listar_usuarios()
        for u in usuarios:
            print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]} ")
            
    elif opcao == "3":
        id_at = input("ID para atualizar: ")
        novo_e = input("Novo Email: ")
        atualizar_email(id_at, novo_e)
        print("✔️ Email atualizado!")

    elif opcao == "4":
        id_del = input("ID para remover: ")
        deletar_usuario(id_del)
        print("🗑️ Usuário removido!")


    elif opcao == "5":
        termo = input("Digite o nome (ou parte dele) para buscar: ")
        resultados = buscar_usuario(termo)
        
        if resultados:
            print(f"\n🔍 Resultados para '{termo}':")
            for u in resultados:
                print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")
        else:
            print(f"\n❌ Nenhum usuário encontrado com o nome '{termo}'.")

    elif opcao == "6":
        dados = exportar_dados()
        
        # O comando 'with open' cria o arquivo no seu computador
        with open("meu_relatorio.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("📋 LISTA DE USUÁRIOS CADASTRADOS\n")
            arquivo.write("-" * 30 + "\n")
            
            for linha in dados:
                arquivo.write(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}\n")
        
        print("✅ Arquivo 'meu_relatorio.txt' criado com sucesso!")