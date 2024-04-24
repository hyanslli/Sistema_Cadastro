import re

class Endereco:
    def __init__(self, rua, numero_Casa, bairro, cidade, estado, cep):
        self.__rua = rua
        self.__numero_Casa = numero_Casa
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = self.validar_Cep(cep)

    def validar_Cep(self, cep):
        if not re.match(r'^\d{5}\-\d{3}$', cep):
            raise ValueError(f'CEP inválido - {cep}')
        return cep

    @property
    def endereco(self):
        endereco = {}
        lista = [self.__rua, self.__numero_Casa, self.__bairro, self.__cidade, self.__estado]
        endereco[self.__cep] = lista

        return endereco
    
    @endereco.setter
    def setEndereco(self, novoCep = None, rua = None, numero_Casa = None,  bairro = None, cidade = None, estado = None):
        if novoCep:
            self.__cep = novoCep
            if rua and numero_Casa and bairro and cidade and estado:
                self.__rua = rua
                self.__numero_Casa = numero_Casa
                self.__bairro = bairro
                self.__cidade = cidade
                self.__estado = estado
            else:
                raise ValueError(f'Campo necessario '+('Rua' if rua is None else "")+('Número da casa' if numero_Casa is None else "")
                                 +('Bairro' if bairro is None else "")+('Bairro' if bairro is None else "")
                                  +('Cidade' if cidade is None else "")+('Estado' if estado is None else ""))