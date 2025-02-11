import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random  # Apenas para simular dados do gráfico; no futuro, integrar com o banco de dados ou API

def create_tab(tab_control):
    tab = tk.Frame(tab_control)
    
    # Cabeçalho do Dashboard – Título e indicação visual de status
    header_frame = tk.Frame(tab)
    header_frame.pack(fill='x', pady=5)
    
    lbl_title = tk.Label(header_frame, text="Dashboard de Apostas", font=('Arial', 16, 'bold'))
    lbl_title.pack(side='left', padx=10)

    # Exemplo de status colorido (alerta da banca)
    # A lógica: Se a banca tiver menos apostas (apostadores perderam) exibe verde, se não, vermelho.
    # Aqui a informação é simulada:
    banca_valor = random.randint(0, 100)  # valor simulado
    status_color = "green" if banca_valor < 50 else "red"
    lbl_status = tk.Label(header_frame, text=f"Banca: {banca_valor}", font=('Arial', 14), fg=status_color)
    lbl_status.pack(side='right', padx=10)
    
    # Mini Gráfico: ocupará 1/4 da área do dashboard
    graph_frame = tk.Frame(tab)
    graph_frame.pack(side='top', fill='x', padx=10, pady=5)
    
    fig = Figure(figsize=(4, 2), dpi=100)
    ax = fig.add_subplot(111)
    # Simula uma série histórica com dados aleatórios (os dados reais virão do processamento de apostas)
    data = [random.randint(0, 100) for _ in range(10)]
    ax.plot(data, marker='o', linestyle='-')
    ax.set_title("Performance Recente")
    ax.set_ylabel("Valor")
    ax.set_xlabel("Tempo")
    
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
    
    # Planilha de registros: utilizamos Treeview para exibir os dados
    # Essa planilha não é editável pelo usuário.
    table_frame = tk.Frame(tab)
    table_frame.pack(fill='both', expand=True, padx=10, pady=5)
    
    columns = ("data", "grupo", "horario", "jogos", "valor_aposta", "status")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    
    # Define as colunas, com títulos e largura
    tree.heading("data", text="Data")
    tree.heading("grupo", text="Grupo")
    tree.heading("horario", text="Horário")
    tree.heading("jogos", text="Nº Jogos")
    tree.heading("valor_aposta", text="Valor da Aposta")
    tree.heading("status", text="Status")
    
    tree.column("data", width=100)
    tree.column("grupo", width=100)
    tree.column("horario", width=100)
    tree.column("jogos", width=80)
    tree.column("valor_aposta", width=120)
    tree.column("status", width=80)
    
    # Para exemplificação, insere dados simulados:
    for i in range(1, 16):
        tree.insert("", tk.END, values=(f"2025-02-0{i%10+1}", f"Grupo {i%3+1}", 
                                        f"{12+i%3}:{30+i%10}", f"{i*2}", f"{i*10:.2f}", "OK" if i%2==0 else "ERR" ))
    
    tree.pack(fill='both', expand=True)
    
    # Filtros: Exemplo de filtros acima da planilha. A planilha permanece não editável
    filter_frame = tk.Frame(tab)
    filter_frame.pack(fill='x', padx=10, pady=5)
    
    tk.Label(filter_frame, text="Filtro (por grupo):").pack(side=tk.LEFT, padx=(0,5))
    entry_filter = tk.Entry(filter_frame)
    entry_filter.pack(side=tk.LEFT, padx=(0,20))
    
    def aplicar_filtro():
        filtro = entry_filter.get().strip().lower()
        # Limpa a planilha e insere apenas itens que possuem o filtro no campo 'grupo'
        for item in tree.get_children():
            tree.delete(item)
        # Aqui você integrará com o banco de dados real; enquanto isso, refazemos a inserção simulada:
        for i in range(1, 16):
            grupo_val = f"grupo {i%3+1}".lower()
            if filtro in grupo_val:
                tree.insert("", tk.END, values=(f"2025-02-0{i%10+1}", f"Grupo {i%3+1}", 
                                                f"{12+i%3}:{30+i%10}", f"{i*2}", f"{i*10:.2f}",
                                                "OK" if i%2==0 else "ERR" ))
    btn_filtrar = tk.Button(filter_frame, text="Aplicar Filtro", command=aplicar_filtro)
    btn_filtrar.pack(side=tk.LEFT, padx=5)
    
    return tab