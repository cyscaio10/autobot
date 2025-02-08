import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class LearningTab:
    def __init__(self, tab_control):
        self.tab = tk.Frame(tab_control)
        self.create_widgets()

    def create_widgets(self):
        self.lbl = tk.Label(self.tab, text="Learning")
        self.lbl.pack(pady=10)

        self.load_image_btn = tk.Button(self.tab, text="Load Image", command=self.load_image)
        self.load_image_btn.pack(pady=10)

        self.canvas = tk.Canvas(self.tab, width=800, height=600)
        self.canvas.pack()

        self.instruction_lbl = tk.Label(self.tab, text="Click and drag to draw a rectangle around the area of interest.")
        self.instruction_lbl.pack(pady=10)

        self.save_btn = tk.Button(self.tab, text="Save Annotation", command=self.save_annotation)
        self.save_btn.pack(pady=10)

        self.annotations = []

    def load_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        end_x = event.x
        end_y = event.y
        self.annotations.append((self.start_x, self.start_y, end_x, end_y))
        self.save_annotation()

    def save_annotation(self):
        # Save the annotations to a file or database
        print("Annotations saved:", self.annotations)

def create_tab(tab_control):
    tab = LearningTab(tab_control)
    return tab.tab