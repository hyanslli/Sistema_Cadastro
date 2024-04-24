import uuid
import re
from Pessoa import Pessoa
from Disciplina import Disciplina

class Professor(Pessoa):
    def __init__(self, nome, cpf, email, rua, numero_Casa, bairro, cidade, estado, cep, nome_disciplina, carga_horaria, horario, numero_sala, bloco, capacidade):
        super().__init__(nome, cpf, email, rua, numero_Casa, bairro, cidade, estado, cep)
        self.disciplina = Disciplina(nome_disciplina, carga_horaria, horario, numero_sala, bloco, capacidade)
        self.id = self.__gerar_id()

    def __gerar_id(self):
        id_gerado = uuid.uuiid4()
        str_id = str(id_gerado).replace('-','')
        trocando_id = str_id[:9]
        numero_id = re.sub(r'\D', '', trocando_id)
        id = '263' + numero_id

        return id
