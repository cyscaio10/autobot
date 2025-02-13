import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AutobotTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Área para exibição de prints
        self.print_frame = ttk.Frame(self)
        self.print_frame.pack(side="left", fill="both", expand=True)

        self.print_canvas = tk.Canvas(self.print_frame)
        self.print_canvas.pack(fill="both", expand=True)

        # Área para controles e inputs
        self.control_frame = ttk.Frame(self)
        self.control_frame.pack(side="right", fill="y")

        ttk.Label(self.control_frame, text="Grupo:").pack()
        self.grupo_entry = ttk.Entry(self.control_frame)
        self.grupo_entry.pack()

        ttk.Label(self.control_frame, text="Data e Hora:").pack()
        self.data_hora_entry = ttk.Entry(self.control_frame)
        self.data_hora_entry.pack()

        ttk.Label(self.control_frame, text="Time:").pack()
        self.time_entry = ttk.Entry(self.control_frame)
        self.time_entry.pack()

        ttk.Label(self.control_frame, text="Odd:").pack()
        self.odd_entry = ttk.Entry(self.control_frame)
        self.odd_entry.pack()

        ttk.Label(self.control_frame, text="Valor:").pack()
        self.valor_entry = ttk.Entry(self.control_frame)
        self.valor_entry.pack()

        self.submit_button = ttk.Button(self.control_frame, text="Submeter", command=self.submit_data)
        self.submit_button.pack(pady=10)

    def display_print(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.print_canvas.create_image(0, 0, anchor="nw", image=photo)
        self.print_canvas.image = photo  # Keep a reference

    def submit_data(self):
        # Implementar lógica para submeter dados para aprendizado
        data = {
            "grupo": self.grupo_entry.get(),
            "data_hora": self.data_hora_entry.get(),
            "time": self.time_entry.get(),
            "odd": self.odd_entry.get(),
            "valor": self.valor_entry.get()
        }
        # Enviar dados para o sistema de aprendizado
        print(f"Dados submetidos: {data}")

