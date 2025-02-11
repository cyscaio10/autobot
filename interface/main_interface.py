import tkinter as tk
from tkinter import ttk, messagebox
from .notification import create_notification_system
from .dashboard_tab import create_tab as create_dashboard_tab
from .logs_tab import create_tab as create_logs_tab
from .settings_tab import create_tab as create_settings_tab
from .configuration_tab import ConfigurationTab
from modules.websocket_manager import WebSocketManager

class MainInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoBot")
        self.root.geometry("1200x800")
        
        # Inicializar WebSocket
        self.ws_manager = WebSocketManager()
        self.setup_websocket_handlers()
        self.ws_manager.start()
        
        # Criar barra superior estilo navegador
        self.create_toolbar()
        
        # Criar notebook para as abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        
        # Inicializar as abas
        self.init_tabs()
        
        self.notification_system = create_notification_system(self.root)        
    def setup_websocket_handlers(self):
        """Configura os handlers para eventos WebSocket"""
        self.ws_manager.register_callback('print_request', self.handle_print_request)
        self.ws_manager.register_callback('automation_status', self.handle_automation_status)
        self.ws_manager.register_callback('question', self.handle_automation_question)
        
    async def handle_print_request(self, data):
        """Lida com solicitações de prints da automação"""
        image_path = data.get('image_path')
        question = data.get('question')
        
        # Usar thread-safe call para atualizar UI
        self.root.after(0, lambda: self.autobot_tab.display_print(image_path, question))
        
        return {'status': 'received'}
        
    async def handle_automation_status(self, data):
        """Atualiza o status da automação na interface"""
        status = data.get('status')
        message = data.get('message')
        
        # Atualizar UI de acordo com o status
        self.root.after(0, lambda: self.update_automation_status(status, message))
        
        return {'status': 'updated'}
        
    async def handle_automation_question(self, data):
        """Processa perguntas da automação"""
        question = data.get('question')
        image_path = data.get('image_path')
        
        # Exibir pergunta na aba AutoBot
        self.root.after(0, lambda: self.autobot_tab.show_question(question, image_path))
        
        return {'status': 'question_received'}        
    def init_tabs(self):
        # Removidas as referências aos arquivos deletados
        dashboard_tab = create_dashboard_tab(self.notebook)
        self.notebook.add(dashboard_tab, text="Dashboard")
        
        logs_tab = create_logs_tab(self.notebook)
        self.notebook.add(logs_tab, text="Logs")
        
        settings_tab = create_settings_tab(self.notebook)
        self.notebook.add(settings_tab, text="Configurações")
        
        group_config_tab = create_group_config_tab(self.notebook)
        self.notebook.add(group_config_tab, text="Grupos")
        
        self.autobot_tab = self.create_autobot_tab()
        self.notebook.add(self.autobot_tab, text="AutoBot")
        
        self.chickenbet_tab = self.create_chickenbet_tab()
        self.notebook.add(self.chickenbet_tab, text="The New ChickenBet")        
    def toggle_automation(self):
        """Ativa/desativa a automação com base nas funções selecionadas"""
        if not self.conferencia_var.get() and not self.atendimento_var.get():
            messagebox.showwarning("Aviso", "Selecione pelo menos uma função para ativar")
            return
            
        # Aqui será implementada a lógica de ativação da automação
        
    def update_automation_state(self):
        """Atualiza estado dos botões baseado nas seleções"""
        if self.atendimento_var.get() and not self.conferencia_var.get():
            messagebox.showwarning("Aviso", "Atendimento requer Conferência ativa")
            self.atendimento_var.set(False)
    
    def create_autobot_tab(self):
        # Implementação da aba AutoBot
        return tk.Frame(self.notebook)

    def add_notification(self, message):
        self.notification_system.add_notification(message)

def start_interface():
    main_interface = MainInterface()
    main_interface.root.mainloop()