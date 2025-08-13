# main.py
import classes as c

def main():
    proprietario = c.Pessoa(nome="", cpf="", email="", telefone="", endereco="")

    carro = c.Veiculo(modelo="", fabricante="", cor="", placa="", ano="", proprietario=proprietario)

    print("DADOS DO PROPRIETÁRIO:")
    proprietario.nome = input("Informe o nome: ").strip().title()
    proprietario.cpf = input("Informe o CPF: ").strip()
    proprietario.email = input("Informe o e-mail: ").strip()
    proprietario.telefone = input("Informe o telefone: ").strip()
    proprietario.endereco = input("Informe o endereço: ").strip().title()

    print("\nDADOS DO VEÍCULO:")
    carro.fabricante = input("Informe o fabricante: ").strip().title()
    carro.modelo = input("Informe o modelo: ").strip().title()
    carro.cor = input("Informe a cor do carro: ").strip().title()
    carro.placa = input("Informe a placa: ").strip().upper()
    carro.ano = input("Informe o ano: ").strip()

    # Atualiza o proprietário após inputs
    carro.proprietario = proprietario

    print("\nDados cadastrados do Proprietário:")
    print(proprietario.obter_dados(), "\n")

    print("Dados cadastrados do Veículo:")
    print(carro.obter_dados())

if __name__ == "__main__":
    main()
