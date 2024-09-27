import tkinter as tk
from tkinter import messagebox, PhotoImage
from tkinter import ttk
import json
import os
from interfaz import CustomStyle

USER_DATA_FILE = 'usuarios.json'

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Economía del Hogar")
        self.geometry("500x700")  # Ajustamos el tamaño para incluir más elementos
        self.resizable(True, True)

        self.iconbitmap("LOGO.ico")
        self.custom_style = CustomStyle()

        style = ttk.Style()
        style.configure("Yellow.TButton", background="yellow", foreground="black", padding=5)
        style.map("Yellow.TButton", background=[('active', 'orange')])

        style.configure("Yellow.TEntry", background="yellow", foreground="black", padding=5)
        
        self.add_top_bar()
        self.load_login_window()

    def add_top_bar(self):
        top_frame = ttk.Frame(self, style="TFrame")
        top_frame.pack(side="top", fill="x")

        logo_image = tk.PhotoImage(file="LOGO.png")
        logo_label = ttk.Label(top_frame, image=logo_image, style="TLabel")
        logo_label.image = logo_image
        logo_label.pack(side="left", padx=10)

        title_label = ttk.Label(top_frame, text="Economía del Hogar", font=("Arial", 16, "bold"), style="TLabel")
        title_label.pack(side="left", padx=5)

        button_minimize = ttk.Button(top_frame, text="—", command=self.iconify, style="TButton")
        button_minimize.pack(side="right", padx=5)

        button_restore = ttk.Button(top_frame, text="⚪", command=self.restore_window, style="TButton")
        button_restore.pack(side="right", padx=5)

        button_maximize = ttk.Button(top_frame, text="⬜", command=self.maximize_window, style="TButton")
        button_maximize.pack(side="right", padx=5)

        button_close = ttk.Button(top_frame, text="✖", command=self.quit, style="TButton")
        button_close.pack(side="right", padx=5)

    def restore_window(self):
        self.state('normal')

    def maximize_window(self):
        if self.state() == 'normal':
            self.state('zoomed')
        else:
            self.state('normal')

    def load_login_window(self):
        for widget in self.winfo_children():
            widget.destroy()

        login_frame = ttk.Frame(self, style="TFrame")
        login_frame.pack(expand=True, pady=20)

        welcome_label = ttk.Label(
            login_frame, 
            text="¡Bienvenido a tu software de gestión para la economía de tu hogar!", 
            font=("Arial", 8), 
            wraplength=116,  
            anchor="center",  
            style="TLabel"
        )
        welcome_label.pack(pady=(10, 5), padx=(20, 0))

        login_message = ttk.Label(
            login_frame, 
            text="Inicia sesión para comenzar", 
            font=("Arial", 8),  
            wraplength=116,  
            anchor="center",  
            style="TLabel"
        )
        login_message.pack(pady=(0, 10))

        self.username_entry = ttk.Entry(login_frame, width=15, font=("Arial", 12))
        self.username_entry.pack(pady=(10, 5), padx=(20, 20))
        self.username_entry.insert(0, "Usuario")
        self.username_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.username_entry, "Usuario"))
        self.username_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.username_entry, "Usuario"))

        self.password_entry = ttk.Entry(login_frame, show="*", width=15, font=("Arial", 12))
        self.password_entry.pack(pady=(10, 20), padx=(20, 20))
        self.password_entry.insert(0, "Contraseña")
        self.password_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.password_entry, "Contraseña"))
        self.password_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.password_entry, "Contraseña"))

        login_button = ttk.Button(
            login_frame, text="INGRESAR", 
            command=self.login, 
            style="Yellow.TButton"
        )
        login_button.pack(pady=20, ipadx=3, ipady=3)

        no_account_message = ttk.Label(
            login_frame, 
            text="¿No tienes una cuenta todavía?", 
            font=("Arial", 11), 
            style="TLabel"
        )
        no_account_message.pack(pady=(10, 5))

        register_button = ttk.Button(
            login_frame, 
            text="Registrarme", 
            command=self.load_register_window, 
            style="Yellow.TButton"
        )
        register_button.pack(pady=10, ipadx=3, ipady=3)
        

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def set_placeholder(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.check_credentials(username, password):
            self.load_main_window(username)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def check_credentials(self, username, password):
        if not os.path.exists(USER_DATA_FILE):
            return False

        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
            return users.get(username) == password

    def load_register_window(self):
        for widget in self.winfo_children():
            widget.destroy()

        register_frame = ttk.Frame(self, style="TFrame")
        register_frame.pack(expand=True, pady=20)

        register_label = ttk.Label(
            register_frame, 
            text="Registrarse", 
            font=("Arial", 16, "bold"), 
            style="TLabel"
        )
        register_label.pack(pady=(10, 10))

        self.new_username_entry = ttk.Entry(register_frame, width=15, font=("Arial", 12))
        self.new_username_entry.pack(pady=(10, 5), padx=(20, 20))

        self.new_password_entry = ttk.Entry(register_frame, show="*", width=15, font=("Arial", 12))
        self.new_password_entry.pack(pady=(10, 20), padx=(20, 20))

        register_button = ttk.Button(
            register_frame, text="Registrarse", 
            command=self.register_user, 
            style="Yellow.TButton"
        )
        register_button.pack(pady=20, ipadx=3, ipady=3)
        

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if username and password:
            if len(password) < 6:  # Verificación de longitud de contraseña
                messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres. Debe incluir Letra mayúscula, un número y signo de puntuación")
                return
            if not os.path.exists(USER_DATA_FILE):
                with open(USER_DATA_FILE, 'w') as file:
                    json.dump({}, file)

            with open(USER_DATA_FILE, 'r+') as file:
                users = json.load(file)
                if username in users:
                    messagebox.showerror("Error", "El usuario ya existe.")
                else:
                    users[username] = password
                    file.seek(0)
                    json.dump(users, file)
                    messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
                    self.load_login_window()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

    def load_main_window(self, username):
        for widget in self.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(self, style="TFrame")
        main_frame.pack(expand=True, fill="both")

        welcome_label = ttk.Label(
            main_frame, 
            text=f"Bienvenido, {username}", 
            font=("Arial", 16), 
            style="TLabel"
        )
        welcome_label.pack(pady=20)
        

        manage_frame = ttk.Frame(main_frame)
        manage_frame.pack(pady=20, padx=20, fill="both")
        

        # Cuadrado para ingresar el nombre
        self.name_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8))
        self.name_entry.insert(0, "▶ Nombre")
        self.name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.name_entry, "▶ Nombre"))
        self.name_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.name_entry, "▶ Nombre"))
        self.name_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))

        # Ingreso
        self.ingreso_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8))
        self.ingreso_entry.insert(0, "▶ Ingreso")
        self.ingreso_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.ingreso_entry, "▶ Ingreso"))
        self.ingreso_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.ingreso_entry, "▶ Ingreso"))
        self.ingreso_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))

        # Campo de gastos
        self.gastos_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8))
        self.gastos_entry.insert(0, "▶ Gastos")
        self.gastos_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.gastos_entry, "▶ Gastos"))
        self.gastos_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.gastos_entry, "▶ Gastos"))
        self.gastos_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))
 

        # Monto
        self.monto_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8))
        self.monto_entry.insert(0, "▶ Monto")
        self.monto_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.monto_entry, "▶ Monto"))
        self.monto_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.monto_entry, "▶ Monto"))
        self.monto_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))

        # Botón para agregar ingreso
        add_button = ttk.Button(
            manage_frame, text="AGREGAR", 
            command=self.add_entry, 
            style="Yellow.TButton"
        )
        add_button.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))

        # Campo de entrada para Editar grupo familiar
        edit_group_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8), style="Yellow.TEntry")
        edit_group_entry.insert(0, "Editar grupo familiar")
        edit_group_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))

        # Campo de entrada para Visualizar Archivo .XLSX
        view_file_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8 ), style="Yellow.TEntry", justify="left")
        view_file_entry.insert(0, "Visualizar Archivo .XLSX ")
        view_file_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5),ipadx=1)

        # Campo de entrada para Editar Registro
        edit_record_entry = ttk.Entry(manage_frame, width=20, font=("Inter", 8), style="Yellow.TEntry")
        edit_record_entry.insert(0, "Editar Registro ")
        edit_record_entry.pack(side="top", anchor="w", padx=(0, 20), pady=(10, 5))
        
        # Botón para cerrar sesión, desplazado más abajo
        logout_button = ttk.Button(
            manage_frame, text="CERRAR SESIÓN", 
            command=self.logout, 
            style="Yellow.TButton"
        )
        logout_button.pack(side="top", anchor="center", padx=(0, 20), pady=(240, 5))  # Aumentar el padding superior

    def add_entry(self):
        name = self.name_entry.get()
        income = self.ingreso_entry.get()
        amount = self.monto_entry.get()

        if name and income and amount:
            # Lógica para agregar la entrada aquí
            messagebox.showinfo("Éxito", "Ingreso agregado correctamente.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.ingreso_entry.delete(0, tk.END)
        self.monto_entry.delete(0, tk.END)

    def logout(self):
        self.load_login_window()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()



