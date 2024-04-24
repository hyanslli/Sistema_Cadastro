import uuid
import re
from Sala import Sala

class Disciplina:
    def __init__(self, nome_Disciplina, carga_Horaria, horario):
        self.__nome_Disciplina = nome_Disciplina
        self.__carga_Horaria = carga_Horaria
        self.__horario = horario
        self.id = self.__gerar_id()

    def __gerar_id(self):
        id_gerado = uuid.uuiid4()
        str_id = str(id_gerado).replace('-','')
        trocando_id = str_id[:5]
        numero_id = re.sub(r'\D', '', trocando_id)
        id = '012' + numero_id

        return id

    @property
    def nome_Disciplina(self):
        return self.__nome_Disciplina
    
    @property
    def carga_Horaria(self):
        return self.__carga_Horaria
    
    @property
    def horario(self):
        return self.__horario