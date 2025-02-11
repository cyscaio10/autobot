import tkinter as tk
from tkinter import ttk

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None

class NotificationSystem:
    def __init__(self, parent):
        self.parent = parent
        self.notifications = []
        self.create_widgets()
        
    def create_widgets(self):
        # Cria o frame para o ícone do sino e o badge de contagem.
        self.icon_frame = tk.Frame(self.parent)
        self.icon_frame.pack(side="top", anchor="ne", padx=10, pady=10)
        
        # Tenta carregar a imagem do sino; se falhar, usa um ícone Unicode.
        if Image and ImageTk:
            try:
                bell_img = Image.open("assets/bell.png")
                bell_img = bell_img.resize((24, 24), Image.ANTIALIAS)
                self.bell_icon = ImageTk.PhotoImage(bell_img)
            except Exception as e:
                print("Erro ao carregar assets/bell.png, usando ícone padrão:", e)
                self.bell_icon = None
        else:
            self.bell_icon = None
        
        if self.bell_icon:
            self.icon_label = tk.Label(self.icon_frame, image=self.bell_icon, cursor="hand2")
        else:
            self.icon_label = tk.Label(self.icon_frame, text="\U0001F514", font=("Arial", 18), cursor="hand2")
        self.icon_label.pack(side="left")
        
        # Badge com contagem de notificações
        self.badge_label = tk.Label(
            self.icon_frame,
            text="0",
            bg="red",
            fg="white",
            font=("Arial", 10, "bold"),
            width=2
        )
        self.badge_label.pack(side="left", padx=(0, 10))
        
        # Painel para exibir as notificações (fila)
        self.notification_panel = tk.Frame(self.parent, bd=2, relief="sunken")
        self.notification_panel.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        
        self.listbox = tk.Listbox(self.notification_panel, font=("Arial", 10))
        self.listbox.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(self.notification_panel, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Opcional: Clique no ícone para limpar notificações
        self.icon_label.bind("<Button-1>", lambda e: self.clear_notifications())
    
    def add_notification(self, message):
        """Adiciona uma mensagem à fila de notificações e atualiza o badge."""
        self.notifications.append(message)
        self.listbox.insert("end", message)
        self.update_badge()
        
    def update_badge(self):
        """Atualiza o badge de contagem de notificações."""
        count = len(self.notifications)
        self.badge_label.config(text=str(count))
        
    def clear_notifications(self):
        """Limpa todas as notificações."""
        self.notifications.clear()
        self.listbox.delete(0, "end")
        self.update_badge()

def create_notification_system(root):
    """
    Cria e retorna uma instância do sistema de notificações persistentes.
    Este sistema exibe um painel com um ícone de sino e um badge
    que indica a quantidade de notificações pendentes. 
    Utiliza uma fila de notificações, e foi pensado para estar presente
    na aba Learning.
    """
    return NotificationSystem(root)
