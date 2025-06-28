"""
# TODO - Atividade: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Altere os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário
- Saia do programa
# NOTE - Dados do Usuário:
- Nome Completo
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Gênero
- Data do cadastro
- Hora do cadastro
"""
import os
import datetime 
from datetime import date

usuarios = []

while True:
    try:       
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Cadastre um novo usuário.")
        print("2 - Liste todos os usuários cadastrados")
        print("3 - Altere os dados de um usuário")
        print("4 - Sortear um usuário")
        print("5 - Exclua um usuário")
        print("6 - Saia do programa")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name =="nt" else "clear")

        match opcao:
            case "1":
                try:
                    hoje = date.today().strftime("%d/%m/%Y")
                    hora = datetime.datetime.now().strftime("%H:%M:%S")
                    usuario = {}
                    usuario['nome'] = input("Informe o nome completo: ").strip()
                    usuario['nascimento'] = input("Informe a data de nascimento: ").strip()
                    usuario['email'] = input("Informe o E-mail: ").strip()
                    usuario['CPF'] = input("Informe o CPF: ").strip()
                    usuario['telefone'] = input("Informe o telefone: ").strip()
                    usuario['genero'] = input("Informe o Gênero: masculino/feminino ").strip()
                    usuario['data'] = hoje
                    usuario['hora'] = hora
                    usuarios.append(usuario)
                except Exception as e:
                    print(f"Não foi possível cadastrar usuário. {e}.")
                finally:
                    continue

            case "2":
                try:
                    for i in range(len(usuarios)):
                        print("-"*40)
                        print(f"Índice {i}: ")
                        for chave in usuario:
                            print(f"    {chave.capitalize()}: {usuario.get(chave)}")
                except Exception as e:
                    print(f"Não foi possível listar os usuários. {e}.")
                finally:
                    continue
            
            case "3":
                try:
                    sair = "s"
                    i = int(input("Informe o indice do usuário que deseja alterar: "))
                    if i >= 0 and i < len(usuarios):
                        for chave in usuario:
                            print(f"{chave.capitalize()}: {usuario.get(chave)}")
                        while sair == "s":
                            try:
                                chave = input("Informe a chave que deseja alterar: ").lower().strip()
                                if chave in usuario:
                                    usuario[chave] = input(f"Informe o novo valor de {chave}: ").strip()
                                    print("Chave alterada")
                                    sair = input("Deseja alterar outra chave: s/n ").lower().strip()
                                else:
                                    print("Chave inexistente.")
                                
                            except Exception as e:
                                print(f"Não foi possível lista o usuário. {e}.")
                            finally:
                                continue
                    
                except Exception as e:
                    print(f"Não foi possível listar os usuários. {e}.")
                finally:
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

