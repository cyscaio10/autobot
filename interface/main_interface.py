import tkinter as tk
from interface import automation_tab, rules_tab, settings_tab, dashboard_tab, learning_tab, configuration_tab, notification

class MainInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Betting Automation System")
        
        self.tab_control = tk.Notebook(root)
        
        self.tab1 = automation_tab.create_tab(self.tab_control)
        self.tab2 = rules_tab.create_tab(self.tab_control)
        self.tab3 = settings_tab.create_tab(self.tab_control)
        self.tab4 = dashboard_tab.create_tab(self.tab_control)
        self.tab5 = learning_tab.create_tab(self.tab_control)
        self.tab6 = configuration_tab.create_tab(self.tab_control)
        
        self.tab_control.add(self.tab1, text='Automation')
        self.tab_control.add(self.tab2, text='Rules')
        self.tab_control.add(self.tab3, text='Settings')
        self.tab_control.add(self.tab4, text='Dashboard')
        self.tab_control.add(self.tab5, text='Learning')
        self.tab_control.add(self.tab6, text='Configuration')
        
        self.tab_control.pack(expand=1, fill='both')
        
        self.notification_system = notification.create_notification_system(root)

    def add_notification(self, message):
        self.notification_system.add_notification(message)

def start_interface():
    root = tk.Tk()
    main_interface = MainInterface(root)
    root.mainloop()