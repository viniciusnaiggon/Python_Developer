"""
# TODO - Atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista= []
"""
import os

nomes = []
while True:
    try:
        # Menu 
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Cadastre novo nome")
        print("2 - Liste todos os nomes na lista")
        print("3 - Pesquise por um nome na lista")
        print("4 - Altere um nome na lista")
        print("5 - Exclua um nome na lista")
        print("6 - Sair do programa")
        # Informe a opção
        opcao = input("Informe a operação desejada: ").strip()
        # lista
        match opcao:
            case "1":
                # Usuário informa nome a ser acrescentado na lista
                try:
                    novo_nome = input("Informe o novo nome: ").title().strip()
                    nomes.append(novo_nome)
                except Exception as e:
                    print(f"Não foi possível Infomar o nome. {e}.")
                finally:
                    for i in range(len(nomes)):
                        print(f"{i}: {nomes[i]}.")
                    continue

            case "2":
                # Exibe a lista
                try:
                    for i in range(len(nomes)):
                        print(f"{i}: {nomes[i]}.")
                except Exception as e:
                    print(f"Não foi possível litar a lista. {e}.")
                finally:
                    for i in range(len(nomes)):
                        print(f"{i}: {nomes[i]}.")
                    continue

            case "3":
                try:
                    nome_pesquisada = input("Informe o nome a ser pesquisado: ").title().strip()
                    qtde = nomes.count(nome_pesquisada)
                    print(f"{nome_pesquisada} foi encontrado {qtde} vezes na lista.")
                except Exception as e:
                    print(f"Não foi possível litar a lista. {e}.")
                finally:
                    continue

            case "4":
                try:
                    # Usuário informa o nome e a posição (índice)
                    i = int(input("Informe a posição do índice a ser alterado: "))

                    if i >= 0 and i <= len(nomes):
                        # Insere novo item em uma posição na lista
                        nomes[i] = input("Informe o novo valor: ").capitalize().strip()
                        print("Nome inserida com sucesso!")
                    else:
                        print("Índice inválido.")
                except Exception as e:
                    print(f"Não foi possível inserir item na lista. {e}.") 
                finally:
                    # Re-exibe a lista e suas posições
                    for i in range(len(nomes)):
                        print(f"Índice {i}: {nomes[i]}.")

            case "5":
                try:
                    i = int(input("Informe a posição do nome na lista: "))
                    if i >= 0 and i < len(nomes):
                        # Exclui nome da lista
                        del(nomes[i])
                        print("Nome excluído com sucesso!")
                    else:
                        print("Posição inválida.")
                except Exception as e:
                    print(f"Não foi possível excluir o nome da lista {e}.")
                finally:
                    # Re-exibe a lista e suas posições
                    for i in range(len(nomes)):
                        print(f"{i}: {nomes[i]}.")
                    continue
            case "6":
                print("Programa encerrado")
                break

            case _:
                os.system("cls" if os.name =="nt" else "clear")
                print("Opção Inválida")
                continue   

    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")




