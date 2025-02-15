import pyautogui
import time

class ChatAutomation:
    def __init__(self, chat_window_title):
        self.chat_window_title = chat_window_title

    def focus_chat_window(self):
        pyautogui.getWindowsWithTitle(self.chat_window_title)[0].activate()

    def send_message(self, message):
        self.focus_chat_window()
        pyautogui.typewrite(message)
        pyautogui.press('enter')

    def capture_chat_screenshot(self):
        self.focus_chat_window()
        screenshot = pyautogui.screenshot()
        return screenshot

    def scroll_chat(self, amount):
        self.focus_chat_window()
        pyautogui.scroll(amount)

    def find_and_click_image(self, image_path, confidence=0.9):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        return False

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


