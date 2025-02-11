import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cv2

class AutoBotTab:
    def __init__(self, tab_control):
        self.tab = tk.Frame(tab_control)
        self.prints_queue = []
        self.current_print = None
        self.create_widgets()
        
    def create_widgets(self):
        # Área principal para exibição de prints e interação
        self.main_frame = tk.Frame(self.tab)
        self.main_frame.pack(fill='both', expand=True)
        
        # Canvas para exibição de prints
        self.canvas = tk.Canvas(self.main_frame, width=800, height=600)
        self.canvas.pack(side='left', fill='both', expand=True)
        
        # Frame para controles e feedback
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(side='right', fill='y')
        
        # Área de resposta para dúvidas da automação
        self.response_frame = tk.LabelFrame(self.control_frame, text="Resposta")
        self.response_frame.pack(fill='x', padx=5, pady=5)
        
        self.response_var = tk.StringVar()
        self.response_entry = tk.Entry(self.response_frame, textvariable=self.response_var)
        self.response_entry.pack(fill='x', padx=5, pady=5)
        
        # Botões de ação
        self.btn_confirm = tk.Button(self.control_frame, text="Confirmar", command=self.confirm_action)
        self.btn_confirm.pack(fill='x', padx=5, pady=2)
        
        self.btn_cancel = tk.Button(self.control_frame, text="Cancelar", command=self.cancel_action)
        self.btn_cancel.pack(fill='x', padx=5, pady=2)
        
        # Área de seleção na imagem
        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)
        
    def display_print(self, image_path, question=None):
        """Exibe um print para análise do operador"""
        self.current_print = cv2.imread(image_path)
        if self.current_print is not None:
            # Converter BGR para RGB
            image_rgb = cv2.cvtColor(self.current_print, cv2.COLOR_BGR2RGB)
            # Converter para formato PIL
            image_pil = Image.fromarray(image_rgb)
            # Criar PhotoImage
            self.photo = ImageTk.PhotoImage(image_pil)
            # Exibir no canvas
            self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
            
            if question:
                self.show_question(question)
    
    def show_question(self, question):
        """Exibe uma pergunta para o operador"""
        question_label = tk.Label(self.response_frame, text=question, wraplength=200)
        question_label.pack(before=self.response_entry)
        
    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.selection_rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline='red'
        )
        
    def update_selection(self, event):
        self.canvas.coords(
            self.selection_rect,
            self.start_x, self.start_y,
            event.x, event.y
        )
        
    def end_selection(self, event):
        end_x, end_y = event.x, event.y
        # Armazenar coordenadas da seleção
        self.selection = (
            min(self.start_x, end_x),
            min(self.start_y, end_y),
            max(self.start_x, end_x),
            max(self.start_y, end_y)
        )
        
    def confirm_action(self):
        """Confirma a ação atual (seleção de área ou resposta)"""
        response = {
            'type': 'selection' if hasattr(self, 'selection') else 'text',
            'data': self.selection if hasattr(self, 'selection') else self.response_var.get()
        }
        # Aqui será implementada a lógica para enviar a resposta via WebSocket
        self.clear_current_action()
        
    def cancel_action(self):
        """Cancela a ação atual"""
        self.clear_current_action()
        
    def clear_current_action(self):
        """Limpa a ação atual"""
        if hasattr(self, 'selection'):
            self.canvas.delete(self.selection_rect)
            del self.selection
        self.response_var.set("")
