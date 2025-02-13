<<<<<<< Tabnine <<<<<<<
import tkinter as tk
from tkinter import ttk
from .dashboard_tab import DashboardTab
from .autobot_tab import AutobotTab
from .atendimento_tab import AtendimentoTab
from .configuracao_tab import ConfiguracaoTab

class MainUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoBot - Sistema de Automação de Apostas")
        self.geometry("1200x800")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.dashboard_tab = DashboardTab(self.notebook)
        self.autobot_tab = AutobotTab(self.notebook)
        self.atendimento_tab = AtendimentoTab(self.notebook)
        self.configuracao_tab = ConfiguracaoTab(self.notebook)

        self.notebook.add(self.dashboard_tab, text="Dashboard")
        self.notebook.add(self.autobot_tab, text="AutoBot")
        self.notebook.add(self.atendimento_tab, text="Atendimento")
        self.notebook.add(self.configuracao_tab, text="Configuração")

    def run(self):
        self.mainloop()
>>>>>>> Tabnine >>>>>>># {"source":"chat"}
