import time
import random
import tkinter as tk

class ChatAutomation:
    def __init__(self, chat_interface):
        """
        chat_interface: Instância do componente que controla a exibição dos prints do chat.
        Essa interface deve possuir os métodos abertos para:
          - expandir um print pelo índice (open_full_print)
          - navegar entre os prints na visualização ampliada (show_next e show_prev)
          - retornar o número total de prints (através do atributo prints)
        """
        self.chat_interface = chat_interface

    def human_like_delay(self, min_delay=0.5, max_delay=1.5):
        time.sleep(random.uniform(min_delay, max_delay))

    def expand_and_navigate_prints(self):
        """
        Para imprimir a sequência completa a partir de uma miniatura:
          1. Clica para expandir o primeiro print visível.
          2. Navega (clicando “Próximo”) até que todas as imagens acumuladas (mesmo que nem todas estejam visíveis como thumbnails) sejam percorridas.
          3. Em cada print, pode rodar uma análise (por exemplo, reconhecimento da aposta).
        """
        total = len(self.chat_interface.prints)
        if total == 0:
            print("Nenhum print disponível para processar.")
            return

        # Expande o primeiro print (índice 0)
        print("Expandindo o print na posição 0")
        # Chama a função que cria a janela de visualização para o print selecionado.
        self.chat_interface.open_full_print(0)
        self.human_like_delay()

        # Simula a navegação por todos os prints existentes
        for i in range(1, total):
            # Pode ser adicionado aqui a lógica que cheque se o print atual contém a informação desejada.
            print(f"Navegando para o print {i}")
            self.chat_interface.show_next()
            self.human_like_delay()

        # Volta para o primeiro print, se necessário (ou fecha a visualização ampliada)
        print("Finalizada a navegação entre os prints.")
        self.chat_interface.full_window.destroy()

    def process_prints_for_aposta(self):
        """
        Função integradora que inicia a sequência de expansão e navegação.
        Pode ser chamada tanto pela automação quanto pelo operador quando a
        análise dos prints precisa ser realizada para reconhecimento completo da aposta.
        """
        try:
            self.expand_and_navigate_prints()
            # Aqui se integraria a lógica de análise da imagem (OCR, comparação com padrões, etc.)
            # Ex.: dados = image_recognition.process_print(self.chat_interface.prints[atual_index])
        except Exception as e:
            print(f"Erro durante o processamento dos prints: {e}")


# Exemplo de uso integrado com a interface (aqui usamos o ChatInterface definido para fins de automação)
if __name__ == "__main__":
    # Para fins de teste, assumimos que a classe ChatInterface (do módulo de chat) é semelhante à implementação anterior.
    import os
    from PIL import Image, ImageTk

    class ChatInterface:
        def __init__(self, parent, prints):
            self.parent = parent
            self.prints = prints  # Lista de caminhos para os prints
            self.full_window = None  # Janela de visualização ampliada
            self.current_index = 0
            self.canvas = tk.Canvas(parent, width=800, height=400)
            self.canvas.pack(fill="both", expand=True)
            self._display_thumbnails()

        def _display_thumbnails(self):
            x_offset = 10
            for index, path in enumerate(self.prints):
                try:
                    img = Image.open(path)
                except Exception as e:
                    print(f"Erro ao abrir {path}: {e}")
                    continue

                scale = 0.7
                width, height = img.size
                new_size = (int(width * scale), int(height * scale))
                img = img.resize(new_size, Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(self.canvas, image=photo, cursor="hand2")
                label.image = photo
                # Apenas para visualização; na automação essa função seria disparada por simulação de clique.
                label.bind("<Button-1>", lambda event, i=index: self.open_full_print(i))
                self.canvas.create_window(x_offset, 20, anchor="nw", window=label)
                x_offset += new_size[0] + 10

        def open_full_print(self, index):
            self.current_index = index
            if self.full_window is not None and tk.Toplevel.winfo_exists(self.full_window):
                self.full_window.destroy()
            self.full_window = tk.Toplevel(self.parent)
            self.full_window.title("Visualização Completa do Print")
            self.full_window.bind("<Escape>", lambda event: self.full_window.destroy())

            self.image_label = tk.Label(self.full_window)
            self.image_label.pack(padx=10, pady=10)

            nav_frame = tk.Frame(self.full_window)
            nav_frame.pack(pady=5)
            btn_prev = tk.Button(nav_frame, text="<< Anterior", command=self.show_prev)
            btn_prev.pack(side="left", padx=5)
            btn_next = tk.Button(nav_frame, text="Próximo >>", command=self.show_next)
            btn_next.pack(side="right", padx=5)
            self.display_full_image()

            # Fechar a janela ao clicar fora do conteúdo (ajuste conforme necessário)
            self.full_window.bind("<Button-1>", self._handle_click_outside)

        def _handle_click_outside(self, event):
            # Se o clique não for no label da imagem, fecha a janela
            if event.widget not in (self.image_label,):
                self.full_window.destroy()

        def display_full_image(self):
            path = self.prints[self.current_index]
            try:
                img = Image.open(path)
            except Exception as e:
                print(f"Erro ao abrir {path}: {e}")
                return

            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo

        def show_next(self):
            self.current_index = (self.current_index + 1) % len(self.prints)
            self.display_full_image()

        def show_prev(self):
            self.current_index = (self.current_index - 1) % len(self.prints)
            self.display_full_image()

    # Teste simples
    root = tk.Tk()
    root.title("Teste de Automação: Prints do Chat")
    # Certifique-se de que os caminhos existam; ajuste os caminhos conforme necessário
    prints_list = [os.path.join("imagens", f"print{i}.png") for i in range(1, 7)]
    chat_interface = ChatInterface(root, prints_list)
    automation = ChatAutomation(chat_interface)

    # Inicia a automação após alguns segundos para que a interface seja exibida
    root.after(3000, automation.process_prints_for_aposta)
    root.mainloop()


