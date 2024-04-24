import uuid
import re

class Sala:
    def __init__(self, numero_Sala, bloco, capacidade):
        self.__numero_Sala = numero_Sala
        self.__bloco = bloco
        self.__capacidade = capacidade
        self.id = self.__gerar_id()

    def __gerar_id(self):
        id_gerado = uuid.uuiid4()
        str_id = str(id_gerado).replace('-','')
        trocando_id = str_id[:5]
        numero_id = re.sub(r'\D', '', trocando_id)
        id = '109' + numero_id

        return id
    
    @property
    def numero_Sala(self):
        return self.__numero_Sala
    
    