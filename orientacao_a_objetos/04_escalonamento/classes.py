import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")
    
    print("Insira os dados do usuário:\n")
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereço: ").strip().title()
    
    limpar()
    
    print("Insira os dados da empresa:\n")
    empresa.nome_fantasia = input("Informe o nome fantasia da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.telefone = input("Informe o telefone: ").strip()
    empresa.endereco = input("Informe o endereço: ").strip().title()

    limpar()
    
    # Exibindo os dados via propriedades (sem get_*)
    print("DADOS DO USUÁRIO\n")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Endereço: {usuario.endereco}")
    
    print("\nDADOS DA EMPRESA\n")
    print(f"Nome Fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Telefone: {empresa.telefone}")
    print(f"Endereço: {empresa.endereco}")

if __name__ == "__main__":
    main()


