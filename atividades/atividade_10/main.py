"""
# TODO - atividade: Faça um CRUD (Creat, Read, Update, Delete) em um JSON
Opções do menu:
- Criar novo arquivo JSON (usuário irá informar o diretório).
- Abrir arquivo JSON (usuário irá informar o diretório).
- Cadastrar novo usuário em um JSON.
- Listar todos os usuário de um arquivo JSON.
- Pesquisar usuário através do valor de uma chave em um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa
Dados do usuário>
- Nome
- Data de nascimento
- CPF
- E-mail
- Telefone
- Filme favorito do usuário
"""
import os
import json

usuarios = []
arquivo = ""
while True:
    try:
        usuario = {}
        # Menu 
        if not arquivo:
            print("Nenhum aquivo aberto")
        else:
            print(f"O arquivo {arquivo} está aberto")
            
        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Criar novo arquivo JSON. ")
        print("2 - Abrir arquivo JSON.")
        print("3 - Cadastrar novo usuário em um JSON.")
        print("4 - Listar todos os usuário em um arquivo JSON.")
        print("5 - Pesquisar por um usuário em um arquivo JSON.")
        print("6 - Alterar dados de um usuário em um arquivo JSON.")
        print("7 - Deletar usuário de um arquivo JSON.")
        print("8 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name =="nt" else "clear")

        match opcao:
            case "1":
                arquivo = input("Informe o nome do arquivo: ")
                diretorio = input("Informe o diretório")

                with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo criado com sucesso.")
            
            case "2":
                arquivo = input("Informe o nome do arquivo: ").strip().lower()
                diretorio = input("Informe o diretório: ").strip().lower()
                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    print("Arquivo aberto com sucesso")     

            case "3":
                try:
                    usuario['nome'] = input("Informe o nome: ").strip().title()
                    usuario['data_nascimento'] = input("Informe a data de nascimento: ")
                    usuario['CPF'] = input("Informe o CPF: ")
                    usuario['email'] = input("Informe o email: ").strip().lower()
                    usuario['telefone'] = input("Informe o telefone: ").strip()
                    usuario['filme'] = input("Informe o filme favorito: ")

                    usuarios.append(usuario)
                           
                    with open(f"{diretorio}/{arquivo}.json", "w", encoding="utf-8") as f:
                        json.dump(usuarios, f, ensure_ascii=False, indent=4)
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Usuário cadastrado com sucesso.")            
                except Exception as e:
                    print(f"Não foi possível cadastrar usuário. {e}.")
            
            case "4":
                if not arquivo:
                    print("Nenhum arquivo aberto")

                with open(f"{diretorio}/{arquivo}.json", "r", encoding="utf-8") as f:
                    dados = json.load(f)
                print(f"{'-'*20} USUÁRIOS {'-'*20}")
                for usuario in dados:
                    for chave in usuario:
                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                    print(f"{'-'*40}")
            
            case "5":
                ...

            case "6":
                ...
            
            case "7":
                ...
            
            case "8":
                print("Programa encerrado")
                break
            
            case _:
                os.system("cls" if os.name =="nt" else "clear")
                print("Opção Inválida")
                continue  


    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")


