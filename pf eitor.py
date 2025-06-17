import json
import os

arquivo_estoque = "estoque.json"

if os.path.exists(arquivo_estoque):
    with open(arquivo_estoque, "r", encoding="utf-8") as f:
            estoque_json = json.load(f)
            estoque = {int(k): v for k, v in estoque_json.items()}   
            
else:
    estoque = {}


def salvar_estoque():
    with open(arquivo_estoque, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)


def listar_estoque():
    if not estoque:
        print("\nO estoque está vazio.\n")
    else:
        print("\n--- Itens no estoque: ---")
        for codigo, item in estoque.items():
            print(f"Código: {codigo} - Produto: {item['nome']} | Quantidade: {item['quantidade']} | Descrição: {item['descrição']} | Unidade: {item['unidade']} | Fornecedor: {item['fornecedor']} | Categoria: {item['categoria']}")
            print("\n---------------------")


    
def pesquisar_item_estoque():
    while True:
        try:
            codigo = int(input("Digite o código do item que você deseja buscar: "))
        except ValueError:
            print("Código inválido. Digite apenas números inteiros.")
            continue
        if codigo in estoque:
            item = estoque[codigo]
            print("\n--- Item encontrado ---")
            print(f"Item encontrado - Produto: {item['nome']} | Quantidade: {item['quantidade']} | Descrição: {item['descrição']} | Unidade: {item['unidade']} | Fornecedor: {item['fornecedor']} | Categoria: {item['categoria']}")
            print("------------------------------")
            break
        else:
            print("Item não encontrado no estoque. Tente novamente.")

def adicionar_item_no_estoque():
    while True:
      try:
          codigo = int(input("Informe o codigo do item: "))
      except ValueError:
          print("Código invalido. Digite apenas numeros inteiros.")    
          continue
          
      if codigo in estoque:
           print("Esse código já está cadastrado! Tente outro.")
      else:
            nome = input("Informe o nome do item: ")
            while True:
                try:
                    quantidade = int(input("Informe a quantidade do item: "))
                    if quantidade <= 0:
                        print("A quantidade deve ser maior que zero. Por favor digite um número para a quantidade")
                        continue
                    break
                except ValueError:
                    print("Digite um número válido para a quantidade.")
            descrição = input("Informe a descrição do item: ")
            unidade = input("Informe a unidade do item: ")
            fornecedor = input("Informe o fornecedor do item: ")
            categoria = input("Informe a categoria do item: ")
            estoque[codigo] = {"nome": nome, "quantidade": quantidade, "descrição": descrição, "unidade": unidade, "fornecedor": fornecedor, "categoria": categoria}
            print("\nItem adicionado ao estoque!\n")
            salvar_estoque()
            break

def editar_item_estoque():
    while True:
        try:
            codigo = int(input("Digite o codigo do item que deseja editar: "))
        except ValueError:
            print("Código inválido. Digite apenas números inteiros.")
            continue
        if codigo in estoque:
            nome = input("Digite o novo nome do item: ")
            while True:
                try:
                    quantidade = int(input("Digite a nova quantidade: "))
                    if quantidade <= 0:
                        print("A quantidade deve ser maior que zero.")
                        continue
                    break
                except ValueError:
                    print("Informe um número válido para quantidade.")
            descrição = input("Digite a nova descrição: ")
            unidade = input("Digite a nova unidade: ")
            fornecedor = input("Digite o novo fornecedor: ")
            categoria = input("Digite a nova categoria: ")
            estoque[codigo] = {"nome": nome, "quantidade": quantidade, "descrição": descrição, "unidade": unidade, "fornecedor": fornecedor, "categoria": categoria}
            print("\nItem atualizado com sucesso!\n")
            salvar_estoque()
            break
        else:
            print("Esse item não está no estoque. Tente novamente.")
            

def excluir_item_estoque():
    while True:
        try:
            codigo = int(input("digite o codigo que voce quer excluir: "))
        except ValueError:
            print("Código inválido. Digite apenas números inteiros.")
            continue
        if codigo in estoque:
            confirmacao = input(f"Tem certeza que deseja excluir o item {estoque[codigo]['nome']}? (S/N): ").strip().upper()
            if confirmacao == 'S':
                del estoque[codigo]
                print("\nItem excluído do estoque!\n")
                salvar_estoque()
                break
            else:
                print("Exclusão cancelada.")
        else:
            print("Item não encontrado no estoque. Tente novamente.")

opcaoEstoque = 0
while(opcaoEstoque != 6):
    print("\n--- Menu de Gerenciamento de Estoque ---")
    print("1 - Listar Estoque ")
    print("2 - Pesquisar item do estoque ")
    print("3 - Adicionar item do estoque ")
    print("4 - Editar item do estoque ")
    print("5 - Excluir item do estoque ")
    print("6 - Retornar ao Menu inicial  ")
    print("----------------------------------------")
    try:
        opcaoEstoque = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite um número válido.")
        continue  
    
    if opcaoEstoque == 1:
        listar_estoque()
    elif opcaoEstoque == 2:
        pesquisar_item_estoque()
    elif opcaoEstoque == 3:
        adicionar_item_no_estoque()
    elif opcaoEstoque == 4:
        editar_item_estoque()
    elif opcaoEstoque == 5:
        excluir_item_estoque()
    elif opcaoEstoque == 6:
        print("Voltando ao menu inicial...")
        break
    else:
        print("Opção inválida. Tente novamente.")
