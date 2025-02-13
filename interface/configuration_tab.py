import tkinter as tk
from tkinter import ttk

class ConfigurationTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        # Planilha
        ttk.Label(self.frame, text="Link da Planilha:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.planilha_entry = ttk.Entry(self.frame, width=50)
        self.planilha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Site de apostas
        ttk.Label(self.frame, text="Link do Site de Apostas:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.apostas_entry = ttk.Entry(self.frame, width=50)
        self.apostas_entry.grid(row=1, column=1, padx=5, pady=5)

        # Site de pesquisa
        ttk.Label(self.frame, text="Link do Site de Pesquisa:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.pesquisa_entry = ttk.Entry(self.frame, width=50)
        self.pesquisa_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botão para salvar configurações
        ttk.Button(self.frame, text="Salvar Configurações", command=self.save_config).grid(row=3, column=1, pady=10)

    def save_config(self):
        # Aqui você implementaria a lógica para salvar as configurações
        print("Configurações salvas:")
        print(f"Planilha: {self.planilha_entry.get()}")
        print(f"Site de Apostas: {self.apostas_entry.get()}")
        print(f"Site de Pesquisa: {self.pesquisa_entry.get()}")