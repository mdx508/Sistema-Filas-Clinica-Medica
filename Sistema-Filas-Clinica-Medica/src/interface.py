
import tkinter as tk
from tkinter import ttk, messagebox
from sistema import SistemaClinica


class InterfaceClinica:
    def __init__(self, janela):
        self.sistema = SistemaClinica()
        self.janela = janela

        self.janela.title("Sistema de Filas - Clínica Médica")
        self.janela.geometry("750x600")
        self.janela.resizable(False, False)

        titulo = tk.Label(
            janela,
            text="SISTEMA DE ATENDIMENTO MÉDICO",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        quadro = tk.Frame(janela)
        quadro.pack(pady=10)

        tk.Label(
            quadro,
            text="Especialidade:"
        ).grid(row=0, column=0, padx=5)

        self.especialidade = ttk.Combobox(
            quadro,
            values=["Clínica Geral", "Cardiologia", "Ortopedia"],
            state="readonly",
            width=20
        )
        self.especialidade.current(0)
        self.especialidade.grid(row=0, column=1, padx=5)

        self.especialidade.bind(
            "<<ComboboxSelected>>",
            lambda event: self.atualizar_painel()
        )

        tk.Label(
            quadro,
            text="Categoria:"
        ).grid(row=0, column=2, padx=5)

        self.categoria = ttk.Combobox(
            quadro,
            values=["Normal", "Preferencial"],
            state="readonly",
            width=15
        )
        self.categoria.current(0)
        self.categoria.grid(row=0, column=3, padx=5)

        tk.Button(
            janela,
            text="Emitir Senha",
            command=self.emitir_senha,
            width=20
        ).pack(pady=8)

        tk.Button(
            janela,
            text="Chamar Próximo Paciente",
            command=self.chamar_paciente,
            width=25
        ).pack(pady=8)

        tk.Button(
            janela,
            text="Consultar Histórico",
            command=self.consultar_historico,
            width=20
        ).pack(pady=8)

        self.ultima_senha = tk.Label(
            janela,
            text="Última senha chamada: Nenhuma",
            font=("Arial", 13, "bold")
        )
        self.ultima_senha.pack(pady=12)

        self.quantidade = tk.Label(
            janela,
            text="Pacientes aguardando: 0",
            font=("Arial", 12)
        )
        self.quantidade.pack(pady=5)

        tk.Label(
            janela,
            text="Pacientes na fila:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.lista = tk.Text(janela, width=65, height=13)
        self.lista.pack(pady=5)

        self.atualizar_painel()

    def emitir_senha(self):
        especialidade = self.especialidade.get()
        categoria = self.categoria.get()

        senha = self.sistema.emitir_senha(especialidade, categoria)

        messagebox.showinfo(
            "Senha emitida",
            f"Senha gerada: {senha}"
        )

        self.atualizar_painel()

    def chamar_paciente(self):
        especialidade = self.especialidade.get()

        senha = self.sistema.chamar_proxima(especialidade)

        if senha is None:
            messagebox.showwarning(
                "Fila vazia",
                "Não existem pacientes aguardando nesta especialidade."
            )
            return

        if "-P" in senha:
            categoria = "Preferencial"
        else:
            categoria = "Normal"

        self.ultima_senha.config(
            text=(
                f"Última senha chamada: {senha}\n"
                f"Especialidade: {especialidade}\n"
                f"Categoria: {categoria}"
            )
        )

        self.atualizar_painel()

    def atualizar_painel(self):
        especialidade = self.especialidade.get()
        filas = self.sistema.consultar_filas(especialidade)

        total = len(filas["Preferencial"]) + len(filas["Normal"])

        self.quantidade.config(
            text=f"Pacientes aguardando: {total}"
        )

        self.lista.delete("1.0", tk.END)

        self.lista.insert(tk.END, "=== FILA PREFERENCIAL ===\n")

        for senha in filas["Preferencial"]:
            tempo = self.sistema.tempo_espera(
                especialidade, "Preferencial", senha
            )

            self.lista.insert(
                tk.END,
                f"{senha} - Espera estimada: {tempo} minutos\n"
            )

        self.lista.insert(tk.END, "\n=== FILA NORMAL ===\n")

        for senha in filas["Normal"]:
            tempo = self.sistema.tempo_espera(
                especialidade, "Normal", senha
            )

            self.lista.insert(
                tk.END,
                f"{senha} - Espera estimada: {tempo} minutos\n"
            )

    def consultar_historico(self):
        especialidade = self.especialidade.get()
        historico = self.sistema.consultar_historico(especialidade)

        if not historico:
            messagebox.showinfo(
                "Histórico",
                "Ainda não existem atendimentos registrados."
            )
            return

        texto = f"Histórico - {especialidade}\n\n"

        for item in historico:
            texto += f"{item['senha']} - {item['categoria']}\n"

        messagebox.showinfo(
            "Histórico de atendimentos",
            texto
        )
