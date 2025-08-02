"""
# TODO - Atividade: Crie um programa de aplicativo de banco, onde:
- O usuário cria uma conta no banco com os seguintes dados:
-- Titular da conta
-- CPF do titular
-- Agência
-- Número da conta
-- Saldo 
O usuário pode fazer no programa:
- Consultar dados
- Depositar valor
- Sacar valor
- Imprimir extrato (entende - se: gerar arquivo com os dados da conta)
- Sair do programa
# NOTE - O nome da classe é conta
"""
import funcao as fu
import classe as cl

while True:
    try:
        fu.limpar_tela()

        print(f"{'-'*20} MENU {"-"*20}")
        print("1 - Criar conta.")
        print("2 - Consultar dados.")
        print("3 - Depositar valor.")
        print("4 - Sacar valor.")
        print("5 - Imprimir extrato")
        print("6 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                ...

            case "2":
                ...

            case "3":
                ...

            case "4":
                ...            
            case "5":
                ...
            case "6":
                print("Programa encerrado")
                break
                
            case _:
                print("Opção Inválida")
                input("\nPressione Enter para continuar...")
                continue  
    except Exception as e:
        print(f"Não foi possível realizar requisição. {e}.")
        input("\nPressione Enter para continuar...")