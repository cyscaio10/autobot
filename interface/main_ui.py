import tkinter as tk
from tkinter import ttk, messagebox

# Classe simples de tooltip para exibir informações ao passar o mouse
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.showtip)
        widget.bind("<Leave>", self.hidetip)

    def showtip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, background="yellow", relief="solid",
                         borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack()

    def hidetip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None

# Classe principal que cria a interface
class MainUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoBot - Interface")
        self.root.geometry("1200x800")
        self.create_top_toolbar()
        self.create_notebook_tabs()

    def create_top_toolbar(self):
        # Barra fixa no topo, com aparência de navegador
        self.top_frame = tk.Frame(self.root, bg="#f0f0f0", relief="raised", bd=2)
        self.top_frame.pack(side="top", fill="x")

        # Botão "Ligar Automação" – com destaque visual (um pouco maior)
        self.btn_ligar = tk.Button(
            self.top_frame, text="Ligar Automação",
            command=self.ligar_automacao, height=2, width=20,
            bg="#4CAF50", fg="white"
        )
        self.btn_ligar.pack(side="left", padx=10, pady=5)
        ToolTip(self.btn_ligar, "Ativa a automação com as funções previamente configuradas")

        # Botões de habilitar ou desabilitar funções específicas
        self.atendimento_var = tk.BooleanVar(value=False)
        self.btn_atendimento = tk.Checkbutton(
            self.top_frame, text="Atendimento",
            variable=self.atendimento_var
        )
        self.btn_atendimento.pack(side="left", padx=10, pady=5)
        ToolTip(self.btn_atendimento, "Ativar atendimento (interação direta com apostadores)")

        self.conferencia_var = tk.BooleanVar(value=False)
        self.btn_conferencia = tk.Checkbutton(
            self.top_frame, text="Conferência",
            variable=self.conferencia_var
        )
        self.btn_conferencia.pack(side="left", padx=10, pady=5)
        ToolTip(self.btn_conferencia, "Ativar conferência (reconhecimento e verificação de apostas)")

        # Um botão extra para acessar a configuração global, se necessário
        self.btn_config = tk.Button(
            self.top_frame, text="Configurar", command=self.abrir_configuracao, width=10
        )
        self.btn_config.pack(side="left", padx=10, pady=5)
        ToolTip(self.btn_config, "Acessar configuração global")

    def create_notebook_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(side="top", fill="both", expand=True)

        # Aba "Configuração de Grupos" – onde são definidos os parâmetros e regras das apostas
        self.tab_config_grupos = tk.Frame(self.notebook)
        self.notebook.add(self.tab_config_grupos, text="Config. de Grupos")
        self.populate_tab_config_grupos()

        # Aba "AutoBot" – central de interação para dúvidas, prints para autenticação e aprendizado
        self.tab_autobot = tk.Frame(self.notebook)
        self.notebook.add(self.tab_autobot, text="AutoBot")
        self.populate_tab_autobot()

        # Aba "The New ChickenBet" – dedicada ao disparo de mensagens com variações e configurações
        self.tab_chickenbet = tk.Frame(self.notebook)
        self.notebook.add(self.tab_chickenbet, text="The New ChickenBet")
        self.populate_tab_chickenbet()

    def populate_tab_config_grupos(self):
        lbl = tk.Label(
            self.tab_config_grupos,
            text="Configuração de Grupos:\nDefina os parâmetros de apostas, grupos e demais configurações.",
            font=("Arial", 12)
        )
        lbl.pack(padx=10, pady=10)
        # Aqui podem ser adicionados widgets para editar configurações específicas dos grupos.

    def populate_tab_autobot(self):
        lbl = tk.Label(
            self.tab_autobot,
            text="AutoBot:\nCentral de Automação e aprendizado.\n"
                 "Quando ocorrer dúvidas (ex: odd não identificada, nome ambíguo), será solicitado um print para validação.",
            font=("Arial", 12)
        )
        lbl.pack(padx=10, pady=10)
        
        # Botão para simular uma solicitação de print para autenticação ou validação
        btn_request_print = tk.Button(
            self.tab_autobot, text="Solicitar Print para Validação", command=self.solicitar_print
        )
        btn_request_print.pack(padx=10, pady=5)
        ToolTip(btn_request_print, "Requisita um print da tela para que o operador valide a informação")

    def populate_tab_chickenbet(self):
        lbl = tk.Label(
            self.tab_chickenbet,
            text="The New ChickenBet:\nConfigure os dias, horários, quantidade de envios, grupos e\n"
                 "os parâmetros de variações das mensagens disparadas.",
            font=("Arial", 12)
        )
        lbl.pack(padx=10, pady=10)
        # Exemplo: botão para salvar configurações de disparo de mensagens
        btn_save = tk.Button(
            self.tab_chickenbet, text="Salvar Configurações", command=self.salvar_config_chickenbet
        )
        btn_save.pack(padx=10, pady=5)
        ToolTip(btn_save, "Salva as configurações de envio de mensagens")

    def ligar_automacao(self):
        # Verifica se há conflito entre os modos; não permite ativar atendimento e conferência simultaneamente.
        if self.atendimento_var.get() and self.conferencia_var.get():
            messagebox.showwarning
