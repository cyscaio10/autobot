import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk  # Lembre-se de instalar Pillow: pip install pillow

class ChatInterface:
    def __init__(self, parent, prints):
        """
        parent: frame ou container onde a lista de prints será exibida.
        prints: lista de caminhos (ou objetos) representando as imagens dos prints.
        """
        self.parent = parent
        self.prints = prints  # Lista com os caminhos das imagens
        self.current_index = 0  # Índice para navegação na visualização ampliada
        
        # Canvas (ou frame) para exibir os prints em miniatura
        self.canvas = tk.Canvas(parent, width=800, height=400)
        self.canvas.pack(fill="both", expand=True)
        
        self.display_thumbnails()

    def display_thumbnails(self):
        """Exibe os prints em formato de thumbnail (70% do tamanho original)."""
        x_offset = 10
        for index, path in enumerate(self.prints):
            try:
                img = Image.open(path)
            except Exception as e:
                print(f"Erro ao abrir {path}: {e}")
                continue

            # Reduzimos o tamanho da imagem para 70% do original
            scale = 0.7
            width, height = img.size
            new_size = (int(width * scale), int(height * scale))
            img = img.resize(new_size, Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(img)
            label = Label(self.canvas, image=photo, cursor="hand2")
            label.image = photo  # Mantém a referência para evitar que a imagem desapareça
            label.bind("<Button-1>", lambda event, i=index: self.open_full_print(i))
            self.canvas.create_window(x_offset, 20, anchor="nw", window=label)
            x_offset += new_size[0] + 10  # Define o offset para o próximo print

    def open_full_print(self, index):
        """Abre uma nova janela com a imagem em tamanho real e controles de navegação."""
        self.current_index = index
        self.full_window = Toplevel(self.parent)
        self.full_window.title("Visualização Completa do Print")
        
        # Permite fechar a janela ao pressionar ESC
        self.full_window.bind("<Escape>", lambda event: self.full_window.destroy())
        
        # Área para exibir a imagem ampliada
        self.image_label = Label(self.full_window)
        self.image_label.pack(padx=10, pady=10)
        
        # Botões de navegação
        nav_frame = tk.Frame(self.full_window)
        nav_frame.pack(pady=5)
        btn_prev = Button(nav_frame, text="<< Anterior", command=self.show_prev)
        btn_prev.pack(side="left", padx=5)
        btn_next = Button(nav_frame, text="Próximo >>", command=self.show_next)
        btn_next.pack(side="right", padx=5)
        
        # Exibe a imagem ampliada
        self.display_full_image()
        
        # Permite fechar ao clicar fora (exemplo simples: clicar na janela)
        self.full_window.bind("<Button-1>", self.handle_click_outside)

    def handle_click_outside(self, event):
        """Fecha a janela se o clique não for sobre o label da imagem ou os botões."""
        widget = event.widget
        if widget not in (self.image_label,):
            self.full_window.destroy()

    def display_full_image(self):
        """Mostra a imagem atual em tamanho completo."""
        path = self.prints[self.current_index]
        try:
            img = Image.open(path)
        except Exception as e:
            print(f"Erro ao abrir {path}: {e}")
            return

        photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Mantém a referência

    def show_next(self):
        """Avança para o próximo print na lista."""
        self.current_index = (self.current_index + 1) % len(self.prints)
        self.display_full_image()

    def show_prev(self):
        """Volta para o print anterior na lista."""
        self.current_index = (self.current_index - 1) % len(self.prints)
        self.display_full_image()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Exemplo de Chat: Prints")
    
    # Exemplo de lista de prints (altere os caminhos para as imagens existentes)
    prints = [
        "imagens/print1.png",
        "imagens/print2.png",
        "imagens/print3.png"
    ]
    
    chat_interface = ChatInterface(root, prints)
    root.mainloop()
