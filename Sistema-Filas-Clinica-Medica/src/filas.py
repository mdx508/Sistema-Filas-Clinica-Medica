 
from collections import deque


class FilaAtendimento:
    def __init__(self, especialidade):
        self.especialidade = especialidade

        self.normal = deque()
        self.preferencial = deque()

        self.contador_normal = 0
        self.contador_preferencial = 0

        self.historico = []

    def emitir_senha(self, categoria):

        if categoria == "Normal":
            self.contador_normal += 1
            senha = f"{self.especialidade}-N{self.contador_normal:03d}"
            self.normal.append(senha)

        elif categoria == "Preferencial":
            self.contador_preferencial += 1
            senha = f"{self.especialidade}-P{self.contador_preferencial:03d}"
            self.preferencial.append(senha)

        else:
            raise ValueError("Categoria inválida.")

        return senha

    def chamar_proxima(self):

        # A fila preferencial sempre tem prioridade
        if len(self.preferencial) > 0:
            senha = self.preferencial.popleft()
            categoria = "Preferencial"

        # A fila normal só é atendida quando a preferencial está vazia
        elif len(self.normal) > 0:
            senha = self.normal.popleft()
            categoria = "Normal"

        else:
            return None

        self.historico.append({
            "senha": senha,
            "categoria": categoria
        })

        return senha

    def consultar_filas(self):

        return {
            "Preferencial": list(self.preferencial),
            "Normal": list(self.normal)
        }

    def quantidade_esperando(self):

        return len(self.normal) + len(self.preferencial)

    def tempo_espera(self, categoria, senha):

        if categoria == "Preferencial":
            fila = list(self.preferencial)

        elif categoria == "Normal":
            fila = list(self.normal)

        else:
            return None

        if senha not in fila:
            return None

        posicao = fila.index(senha)

        if categoria == "Normal":
            posicao += len(self.preferencial)

        return posicao * 30
