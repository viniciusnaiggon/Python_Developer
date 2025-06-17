'''
# TODO - Atividade: Crie um programa wue faça as seguintes operações:
- Calcular área de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
# NOTE - Para cada loop, o programa deverá limpar o terminal
'''
import math as m
import os

while True:
    try:
        print(f"{'-'*20} MENU{'-'*20}\n")
        print(f"1 - Calcular área de um círculo")
        print(f"2 - Calcular tamanho de uma circunferência")
        operador = input("Informe a operação desejada: ").strip()
        match operador:
            case "1":
                try:
                    r = float(input("Imforme o valor do raio em cm: "))
                    area = m.pi * (r**2)
                    print(f"O valor da área do círculo com o raio informado de {r} é de {area:.1f}cm")
                except Exception as e:
                    print(f"Não foi possível somar. {e}.")
                break
            case "2":
                try:
                    r = float(input("Imforme o valor do raio em cm: "))
                    cir = (2*m.pi) * r
                    print(f"O valor da circunferência com o raio informado de {r} é de {cir:.1f}cm")
                except Exception as e:
                    print(f"Não foi possível somar. {e}.")
                break

        while True:
            prosseguir = input("Deseja refazer? (s/n): ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida, por favor digite 's' para sim ou 'n' para não.")
            continue

        match prosseguir:
            case "s":
                os.system("cls")
                continue
            case "n":
                os.system("cls")
                break
            case _:
                print("Opção inválida.")
                break

    except Exception as e:
            print(f"Não foi possível calcular o IMC. {e}.")
            continue