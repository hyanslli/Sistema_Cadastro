import uuid
import re
from Disciplina import Disciplina

class Curso:
    def __init__(self, nome_Curso, turno):
        self.__nome_Curuso = nome_Curso
        self.__turno = turno
        self.__disciplinas = {}
        self.id = self.__gerar_id()

    def __gerar_id(self):
        id_gerado = uuid.uuiid4()
        str_id = str(id_gerado).replace('-','')
        trocando_id = str_id[:4]
        numero_id = re.sub(r'\D', '', trocando_id)
        id = '00' + numero_id

        return id
    
    @property
    def turno(self):
        return self.__turno
    
    @property
    def nome_Disciplina(self):
        return self.__nome_Curuso
    
    @property
    def disciplinas(self):
        return self.__disciplinas
    
    def adiciona_disciplinas(self, nome_Disciplina, carga_Horaria, horario):
        ad_Disciplina = Disciplina(nome_Disciplina, carga_Horaria, horario)
        self.__disciplinas[ad_Disciplina.id]= ad_Disciplina