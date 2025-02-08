import tkinter as tk
from tkinter import messagebox

class NotificationSystem:
    def __init__(self, root):
        self.notifications = 0
        self.notification_label = tk.Label(root, text="", fg="red")
        self.notification_label.pack(pady=10)

    def add_notification(self, message):
        self.notifications += 1
        self.notification_label.config(text=f"Notifications: {self.notifications}")
        messagebox.showinfo("Notification", message)

def create_notification_system(root):
    return NotificationSystem(root)