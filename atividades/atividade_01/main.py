'''
# TODO - atividade:
Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o usuário qual o melhor combustível para abastecer.
# NOTE - o usuário poderá informar várias vezes os valores, irá encerrar o programa quando desejar.
# NOTE - cálculo: compensa etanol caso ele tenha 70% do valor da gasolina.
# NOTE - DIVIRTAM-SE!!!
'''

while True:
    # Menu 
    print(f"{'-'*20} MENU {"-"*20}")
    print("1 - Calcular melhor combustível para abastecer ")
    print("2 - Encerrar o programa")

    operador = input("Informe a operação desejada: ").strip()

    match operador:
        case "1":
            try:
                # Entrada de dados
                gasolina = float(input("Informe o valor da gasolina: ").replace(",","."))
                etanol = float(input("Informe o valor do etanol: ").replace(",","."))
                vantagem = (etanol/gasolina)*100
                if vantagem <= 70:
                     print(f"Valor do porcentual {vantagem}%, compensa a etanol")
                else:
                    print(f"Valor do porcentual {vantagem}%, compensa o gasolina")
            except Exception as e:
                print(f"Não foi possível calcular. {e}.")
            finally:
                continue
        case "2":
            print("Programa encerrado")
            break