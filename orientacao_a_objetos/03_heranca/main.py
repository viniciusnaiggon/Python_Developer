import classes as c
import os

# Função para limpar o terminal
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # Instancia as classes corretamente
    pessoa_fisica = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # Input do usuário
    print("Entre com os dados do usuário:\n")
    
    pessoa_fisica.nome = input("Informe o nome: ").strip().title()
    pessoa_fisica.cpf = input("Informe o CPF: ").strip()
    pessoa_fisica.telefone = input("Informe o telefone: ").strip()
    pessoa_fisica.endereco = input("Informe o endereço: ").strip().title()
    
    limpar()
        
    # Input da empresa
    print("Entre com os dados da empresa:\n")
    
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()
    
    # Output
    limpar()
    print("DADOS DO USUÁRIO:")
    pessoa_fisica.exibir_dados()

    print("\nDADOS DA EMPRESA:")
    empresa.exibir_dados()

if __name__ == "__main__":
    main()
