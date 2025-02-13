import tkinter as tk
from tkinter import ttk
from ..modules.group_config import GroupConfig

class ConfigTab(ttk.Frame):
    def __init__(self, parent, group_config):
        super().__init__(parent)
        self.group_config = group_config
        self.create_widgets()

    def create_widgets(self):
        # Criar widgets para adicionar grupos
        self.group_frame = ttk.LabelFrame(self, text="Grupos")
        self.group_frame.pack(fill="x", padx=10, pady=5)

        self.group_entry = ttk.Entry(self.group_frame)
        self.group_entry.pack(side="left", padx=5)

        self.add_group_button = ttk.Button(self.group_frame, text="Adicionar Grupo", command=self.add_group)
        self.add_group_button.pack(side="left")

        # Criar widgets para regras
        self.rules_frame = ttk.LabelFrame(self, text="Regras")
        self.rules_frame.pack(fill="x", padx=10, pady=5)

        self.rules_listbox = tk.Listbox(self.rules_frame)
        self.rules_listbox.pack(fill="x", padx=5, pady=5)

        for rule in self.group_config.rules:
            self.rules_listbox.insert(tk.END, rule)

        # Criar widgets para aplicar regras aos grupos
        self.apply_frame = ttk.LabelFrame(self, text="Aplicar Regras")
        self.apply_frame.pack(fill="x", padx=10, pady=5)

        self.group_combobox = ttk.Combobox(self.apply_frame, values=list(self.group_config.groups.keys()))
        self.group_combobox.pack(side="left", padx=5)

        self.apply_button = ttk.Button(self.apply_frame, text="Aplicar Regra", command=
