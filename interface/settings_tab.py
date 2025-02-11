import tkinter as tk

def create_tab(tab_control):
    tab = tk.Frame(tab_control)
    
    lbl = tk.Label(tab, text="Configurações do Sistema", font=('Arial', 14, 'bold'))
    lbl.pack(pady=10)
    
    # Exemplo de campo para inserir um link
    frm_links = tk.Frame(tab)
    frm_links.pack(pady=5, padx=10, fill='x')
    
    lbl_link = tk.Label(frm_links, text="Link do Site de Apostas:")
    lbl_link.pack(side=tk.LEFT, padx=(0, 5))
    entry_link = tk.Entry(frm_links, width=50)
    entry_link.pack(side=tk.LEFT, fill='x', expand=True)
    
    # Botão para salvar a configuração
    btn_salvar = tk.Button(tab, text="Salvar Configurações")
    btn_salvar.pack(pady=10)
    
    # Outros campos e opções de configuração poderão ser adicionados conforme necessário.
    
    return tab
