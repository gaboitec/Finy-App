import tkinter as tk
from tkinter import messagebox
from logica.usuario_logica import UsuarioService
from gestores.usuarios_gestor import UsuariosRepo

class RegistroView(tk.Frame):
    def __init__(self, master, on_registro_exitoso):
        super().__init__(master)
        self.on_registro_exitoso = on_registro_exitoso
        self.usuario_service = UsuarioService(UsuariosRepo())
        self._construir_interfaz()

    def _construir_interfaz(self):
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        frame = tk.Frame(self, bg="white")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Registro de Usuario", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        tk.Label(frame, text="Nombre:", bg="white").pack(anchor="w")
        self.entry_nombre = tk.Entry(frame, width=30)
        self.entry_nombre.pack(pady=5)

        tk.Label(frame, text="Correo:", bg="white").pack(anchor="w")
        self.entry_correo = tk.Entry(frame, width=30)
        self.entry_correo.pack(pady=5)

        tk.Label(frame, text="Contraseña:", bg="white").pack(anchor="w")
        self.entry_contra = tk.Entry(frame, show="*", width=30)
        self.entry_contra.pack(pady=5)

        btn_registrar = tk.Button(frame, text="Crear cuenta", command=self._registrar_usuario, bg="#FF8000", fg="white")
        btn_registrar.pack(pady=10)

    def _registrar_usuario(self):
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        contra = self.entry_contra.get().strip()

        if not nombre or not correo or not contra:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return

        creado = self.usuario_service.registrar_usuario(nombre, correo, contra)
        if creado:
            messagebox.showinfo("Registro exitoso", "Tu cuenta ha sido creada.")
            self.on_registro_exitoso()
        else:
            messagebox.showerror("Error", "No se pudo crear el usuario. ¿Ya existe?")
