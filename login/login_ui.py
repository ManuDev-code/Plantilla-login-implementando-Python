import tkinter as tk
from tkinter import messagebox
import users
import dashboard_ui

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Iniciar Sesión")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        
        # Configuración de la ventana
        self.root.configure(bg="#f4f4f4")
        
        # Título
        self.title_label = tk.Label(
            root, 
            text="Iniciar Sesión", 
            font=("Arial", 16, "bold"),
            bg="#f4f4f4"
        )
        self.title_label.pack(pady=20)
        
        # Frame para el formulario
        self.frame = tk.Frame(root, bg="#f4f4f4")
        self.frame.pack(pady=10)
        
        # Usuario
        self.username_label = tk.Label(
            self.frame, 
            text="Usuario:", 
            font=("Arial", 10),
            bg="#f4f4f4"
        )
        self.username_label.grid(row=0, column=0, sticky="w", pady=5)
        
        self.username_entry = tk.Entry(self.frame, width=25)
        self.username_entry.grid(row=0, column=1, pady=5)
        
        # Contraseña
        self.password_label = tk.Label(
            self.frame, 
            text="Contraseña:", 
            font=("Arial", 10),
            bg="#f4f4f4"
        )
        self.password_label.grid(row=1, column=0, sticky="w", pady=5)
        
        self.password_entry = tk.Entry(self.frame, width=25, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        
        # Botón de login
        self.login_button = tk.Button(
            root,
            text="Iniciar Sesión",
            command=self.login,
            bg="#4CAF50",
            fg="white",
            width=15,
            height=2
        )
        self.login_button.pack(pady=20)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor, completa todos los campos")
            return
        
        if users.authenticate(username, password):
            messagebox.showinfo("Éxito", f"Bienvenido, {username}!")
            self.root.withdraw()  # Oculta la ventana de login
            self.open_dashboard(username)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def open_dashboard(self, username):
        dashboard_window = tk.Toplevel(self.root)
        dashboard_ui.DashboardWindow(dashboard_window, username, self.root)