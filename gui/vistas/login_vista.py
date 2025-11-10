import tkinter as tk
from tkinter import messagebox
from logica.usuario_logica import UsuarioService
from gestores.usuarios_gestor import UsuariosRepo

class LoginView(tk.Frame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.on_login = on_login
        self.usuario_service = UsuarioService(UsuariosRepo())
        self._construir_interfaz()

    def _construir_interfaz(self):
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        frame = tk.Frame(self, bg="white")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="FINY - Iniciar sesión", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        tk.Label(frame, text="Correo:", bg="white").pack(anchor="w")
        self.entry_correo = tk.Entry(frame, width=30)
        self.entry_correo.pack(pady=5)

        tk.Label(frame, text="Contraseña:", bg="white").pack(anchor="w")
        self.entry_contra = tk.Entry(frame, show="*", width=30)
        self.entry_contra.pack(pady=5)

        btn_login = tk.Button(frame, text="Ingresar", command=self._iniciar_sesion, bg="#FF8000", fg="white")
        btn_login.pack(pady=(10, 5))

        #Registrarse
        btn_registro = tk.Button(frame, text="Registrarse", command=self._abrir_registro, bg="white", fg="#FF8000", bd=0)
        btn_registro.pack()

    def _iniciar_sesion(self):
        """correo = self.entry_correo.get().strip()
        contra = self.entry_contra.get().strip()

        if not correo or not contra:
            messagebox.showwarning("Campos vacíos", "Por favor ingresa tu correo y contraseña.")
            return

        usuario = self.usuario_service.buscar_por_correo(correo, contra)"""
        usuario = self.usuario_service.buscar_por_correo("yefry@correo.com", "hash123")
        if usuario:
            self.on_login(usuario)
        else:
            messagebox.showerror("Error de autenticación", "Correo o contraseña incorrectos.")

    def _abrir_registro(self):
        self.pack_forget()
        self.master.mostrar_registro()

