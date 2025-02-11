import tkinter as tk
from tkinter import ttk

class LearningTab:
    def __init__(self, parent):
        # Cria o frame que será a aba Learning
        self.tab = tk.Frame(parent)
        self.create_widgets()

    def create_widgets(self):
        # Título da aba
        header = tk.Label(self.tab, text="Learning Tab", font=("Helvetica", 16))
        header.pack(pady=10)

        # Área para exibir dados – usando um Treeview como exemplo
        self.tree = ttk.Treeview(self.tab, columns=("Value",), show="headings")
        self.tree.heading("Value", text="Value")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Botão para demonstrar adição de dados na árvore
        add_btn = tk.Button(self.tab, text="Add Data", command=self.add_data)
        add_btn.pack(pady=5)

    def add_data(self):
        # Exemplo de adição de linha com dados fictícios
        self.tree.insert("", "end", values=("Sample Data",))
def create_tab(tab_control):
    lbl = tk.Label(tab, text="Dashboard")
    lbl.pack(pady=10)

  