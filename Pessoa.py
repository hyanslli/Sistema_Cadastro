import re
from Endereco import Endereco

class Pessoa(Endereco):
    def __init__(self, nome, cpf, email, rua, numero_Casa, bairro, cidade, estado, cep):
        super().__init__(rua, numero_Casa, bairro, cidade, estado, cep)
        self.__nome = nome
        self.__cpf = self.__validar_Cpf(cpf)
        self.__email = self.__validar_Email(email)

    def get_Endereco(self):
        return self.endereco
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def setNome(self, novoNome):
        self.__nome = novoNome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def setCpf(self, novoCpf):
        self.__cpf = novoCpf
    
    def __validar_Cpf(self, cpf):
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise ValueError(f'CPF inválido: {cpf}') 
        return cpf

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def setEmail(self, novoEmail):
        self.__email = novoEmail

    def __validar_Email(self, email):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$', email):
            raise ValueError(f'Email inválido: {email}')
        return email

