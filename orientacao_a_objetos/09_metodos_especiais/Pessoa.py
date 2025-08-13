class Pessoa:
    # contrutor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        def __str__(self):
            return f"Ola, meu nome e {self.nome} e tenho {self.idade} anos."
        
        def __len__(self):
            return self.idade