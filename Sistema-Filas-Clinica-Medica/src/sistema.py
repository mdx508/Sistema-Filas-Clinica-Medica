from filas import FilaAtendimento


class SistemaClinica:
    def __init__(self):
        self.especialidades = {
            "Clínica Geral": FilaAtendimento("CG"),
            "Cardiologia": FilaAtendimento("CAR"),
            "Ortopedia": FilaAtendimento("ORT")
        }

    def emitir_senha(self, especialidade, categoria):
        if especialidade not in self.especialidades:
            raise ValueError("Especialidade inválida.")

        return self.especialidades[especialidade].emitir_senha(categoria)

    def chamar_proxima(self, especialidade):
        if especialidade not in self.especialidades:
            raise ValueError("Especialidade inválida.")

        return self.especialidades[especialidade].chamar_proxima()

    def consultar_filas(self, especialidade):
        if especialidade not in self.especialidades:
            raise ValueError("Especialidade inválida.")

        return self.especialidades[especialidade].consultar_filas()


    def tempo_espera(self, especialidade, categoria, senha):
        if especialidade not in self.especialidades:
            raise ValueError("Especialidade inválida.")

        return self.especialidades[especialidade].tempo_espera(
            categoria, senha
        )

      
    def consultar_historico(self, especialidade):
        if especialidade not in self.especialidades:
            raise ValueError("Especialidade inválida.")

        return self.especialidades[especialidade].historico
