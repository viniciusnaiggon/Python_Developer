# Superclasse ou classe-pai
class Pessoa:
    # Construtor
    def __init__(self, telefone, endereco):
        self.telefone = telefone
        self.endereco = endereco
        
        def exibir_dados():
            print(f"Telefone:{self.telefone}")
            print(f"Endereco:{self.endereco}")

# SUBCLASSES OU CLASSE-FILHA
class PessoaFisica(Pessoa):
   def __init__(self, nome, cpf, telefone, endereco):
       self.nome = nome
       self.cpf = cpf
       super().__init__(telefone, endereco)
       
    
    
class PessoaJuridica(Pessoa):
       def __init__(self, nome_fantasia, cnpj, telefone, endereco):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(telefone, endereco)