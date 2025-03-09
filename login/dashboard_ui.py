import tkinter as tk
from tkinter import messagebox

class DashboardWindow:
    def __init__(self, root, username, login_window):
        self.root = root
        self.username = username
        self.login_window = login_window
        
        self.root.title("Panel de Control")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Configuración de la ventana
        self.root.configure(bg="#f4f4f4")
        
        # Título
        self.title_label = tk.Label(
            root, 
            text=f"Bienvenido, {username}!", 
            font=("Arial", 16, "bold"),
            bg="#f4f4f4"
        )
        self.title_label.pack(pady=30)
        
        # Mensaje
        self.message_label = tk.Label(
            root, 
            text="Has iniciado sesión correctamente.", 
            font=("Arial", 12),
            bg="#f4f4f4"
        )
        self.message_label.pack(pady=20)
        
        # Botón de cerrar sesión
        self.logout_button = tk.Button(
            root,
            text="Cerrar Sesión",
            command=self.logout,
            bg="#f44336",
            fg="white",
            width=15,
            height=2
        )
        self.logout_button.pack(pady=20)
        
        # Cuando se cierra la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def logout(self):
        self.root.destroy()
        self.login_window.deiconify()  # Muestra la ventana de login nuevamente
        messagebox.showinfo("Información", "Has cerrado sesión")
    
    def on_close(self):
        self.root.destroy()
        self.login_window.destroy()  # Cierra también la ventana de login