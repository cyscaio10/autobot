import tkinter as tk

def create_tab(tab_control):
    tab = tk.Frame(tab_control)
    
    lbl = tk.Label(tab, text="Dashboard")
    lbl.pack(pady=10)
    
    # Adicione mais controles e widgets aqui
    
    return tab