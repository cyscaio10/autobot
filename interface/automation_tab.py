import tkinter as tk

def create_tab(tab_control):
    tab = tk.Frame(tab_control)
    lbl = tk.Label(tab, text="Automação e Controle", font=('Arial', 14, 'bold'))
    lbl.pack(pady=10)
    
    # Botões de controle
    btn_iniciar = tk.Button(tab, text="Iniciar Automação")
    btn_iniciar.pack(side=tk.LEFT, padx=10, pady=5)
    
    btn_pause = tk.Button(tab, text="Pausar Automação")
    btn_pause.pack(side=tk.LEFT, padx=10, pady=5)
    
    btn_stop = tk.Button(tab, text="Parar Automação")
    btn_stop.pack(side=tk.LEFT, padx=10, pady=5)
    
    # Checkbox para habilitar/desabilitar automação (evita conflitos)
    var_automacao = tk.BooleanVar(value=True)
    chk_automacao = tk.Checkbutton(tab, text="Automação Ligada", variable=var_automacao)
    chk_automacao.pack(side=tk.LEFT, padx=10)
    
    return tab