# classes.py

class Pessoa:
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def obter_dados(self):
        return (
            f"Nome: {self.__nome}\n"
            f"CPF: {self.__cpf}\n"
            f"E-mail: {self.__email}\n"
            f"Telefone: {self.__telefone}\n"
            f"Endereço: {self.__endereco}"
        )


class Veiculo:
    def __init__(self, modelo, fabricante, cor, placa, ano, proprietario):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__cor = cor
        self.__placa = placa
        self.__ano = ano
        self.__proprietario = proprietario

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def ano(self):
        return self.__ano
            
            