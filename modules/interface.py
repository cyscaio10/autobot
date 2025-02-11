import tkinter as tk
from tkinter import ttk

# Importando as abas desenvolvidas
from interface.dashboard_tab import create_tab as create_dashboard_tab
from interface.logs_tab import create_tab as create_logs_tab
from interface.settings_tab import create_tab as create_settings_tab
from interface.rules_tab import create_tab as create_rules_tab
from interface.configuration_tab import ConfigurationTab
from interface.learning_tab import LearningTab
from interface.group_config_tab import create_tab as create_group_config_tab

def main():
    root = tk.Tk()
    root.title("AutoBot")
    
    # Define o ícone usando um arquivo PNG (certifique-se de ter 'assets/autobot_icon.png')
    try:
        root.iconphoto(True, tk.PhotoImage(file="assets/autobot_icon.png"))
    except Exception as e:
        print("Erro ao definir ícone:", e)
    
    # Em Linux, "zoomed" pode não funcionar; se quiser tela cheia, use -fullscreen ou comente essa linha
    # root.state("zoomed")
    root.attributes("-fullscreen", True)
    
    # Criar o Notebook para organizar as abas
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)
    
    # Abas da interface:
    dashboard_tab = create_dashboard_tab(notebook)
    notebook.add(dashboard_tab, text="Dashboard")
    
    logs_tab = create_logs_tab(notebook)
    notebook.add(logs_tab, text="Logs")
    
    settings_tab = create_settings_tab(notebook)
    notebook.add(settings_tab, text="Configurações")
    
    group_config_tab = create_group_config_tab(notebook)
    notebook.add(group_config_tab, text="Grupos")
    
    config_tab_instance = ConfigurationTab(notebook)
    notebook.add(config_tab_instance.tab, text="Apostas")
    
    learning_tab_instance = LearningTab(notebook)
    notebook.add(learning_tab_instance.tab, text="Learning")
    
    rules_tab = create_rules_tab(notebook)
    notebook.add(rules_tab, text="Help")
    
    root.mainloop()

if __name__ == "__main__":
    main()