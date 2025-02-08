import tkinter as tk
from tkinter import ttk

class ConfigurationTab:
    def __init__(self, tab_control):
        self.tab = tk.Frame(tab_control)
        self.create_widgets()

    def create_widgets(self):
        self.lbl = tk.Label(self.tab, text="Group Configuration")
        self.lbl.pack(pady=10)

        self.group_list_frame = tk.Frame(self.tab)
        self.group_list_frame.pack(pady=10, fill='both', expand=True)

        self.load_groups()

    def load_groups(self):
        # Carregar grupos da planilha do Google Sheets
        groups = self.get_groups_from_sheet()
        
        for group in groups:
            self.create_group_frame(group)

    def get_groups_from_sheet(self):
        # Simulação de dados de exemplo
        return [
            {"name": "Group 1", "active": True, "games": 10, "won": 5, "lost": 3, "ongoing": 2, "total_bets": 1000, "total_value": 5000},
            {"name": "Group 2", "active": False, "games": 8, "won": 3, "lost": 4, "ongoing": 1, "total_bets": 800, "total_value": 4000},
            # Adicionar mais grupos conforme necessário
        ]

    def create_group_frame(self, group):
        frame = tk.Frame(self.group_list_frame, borderwidth=1, relief="solid")
        frame.pack(pady=5, padx=5, fill='x')

        name_label = tk.Label(frame, text=group["name"])
        name_label.grid(row=0, column=0, padx=5, pady=5)

        active_label = tk.Label(frame, text="Active" if group["active"] else "Inactive")
        active_label.grid(row=0, column=1, padx=5, pady=5)

        games_label = tk.Label(frame, text=f"Games: {group['games']}")
        games_label.grid(row=0, column=2, padx=5, pady=5)

        won_label = tk.Label(frame, text=f"Won: {group['won']}")
        won_label.grid(row=0, column=3, padx=5, pady=5)

        lost_label = tk.Label(frame, text=f"Lost: {group['lost']}")
        lost_label.grid(row=0, column=4, padx=5, pady=5)

        ongoing_label = tk.Label(frame, text=f"Ongoing: {group['ongoing']}")
        ongoing_label.grid(row=0, column=5, padx=5, pady=5)

        total_bets_label = tk.Label(frame, text=f"Total Bets: {group['total_bets']}")
        total_bets_label.grid(row=0, column=6, padx=5, pady=5)

        total_value_label = tk.Label(frame, text=f"Total Value: {group['total_value']}")
        total_value_label.grid(row=0, column=7, padx=5, pady=5)

        rules_button = tk.Button(frame, text="Rules", command=lambda: self.show_rules(group["name"]))
        rules_button.grid(row=0, column=8, padx=5, pady=5)

    def show_rules(self, group_name):
        # Mostrar regras específicas do grupo em uma nova janela
        rules_window = tk.Toplevel(self.tab)
        rules_window.title(f"Rules for {group_name}")

        rules_list = tk