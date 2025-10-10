import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FINY")
        self.geometry("400x400")
        self.configure(bg="white")
        self._construir_interfaz()

    def _construir_interfaz(self):
        titulo = tk.Label(self, text="FINY", font=("Helvetica", 32, "bold"), fg="#FF8000", bg="white")
        titulo.pack(pady=(40, 20))

        lbl_correo = tk.Label(self, text="Correo:", font=("Helvetica", 12), bg="white")
        lbl_correo.pack(anchor="w", padx=40)
        self.entry_correo = tk.Entry(self, font=("Helvetica", 12), bd=1, relief="solid", width=30)
        self.entry_correo.pack(pady=5)

        lbl_contra = tk.Label(self, text="Contraseña:", font=("Helvetica", 12), bg="white")
        lbl_contra.pack(anchor="w", padx=40, pady=(10, 0))
        self.entry_contra = tk.Entry(self, font=("Helvetica", 12), bd=1, relief="solid", width=30, show="*")
        self.entry_contra.pack(pady=5)

        btn_ingresar = tk.Button(self, text="Ingresar", font=("Helvetica", 12, "bold"), bg="black", fg="white",
                                 width=20, height=2, command=self._iniciar_sesion)
        btn_ingresar.pack(pady=20)

        frame_links = tk.Frame(self, bg="white")
        frame_links.pack(fill="x", padx=40)

        link_olvidada = tk.Label(frame_links, text="Contraseña olvidada", fg="black", bg="white",
                                 font=("Helvetica", 10, "underline"), cursor="hand2")
        link_olvidada.pack(side="left")

        link_crear = tk.Label(frame_links, text="Crear cuenta", fg="#FF8000", bg="white",
                              font=("Helvetica", 10, "underline"), cursor="hand2")
        link_crear.pack(side="right")

    def _iniciar_sesion(self):
        correo = self.entry_correo.get()
        contra = self.entry_contra.get()
        print(f"[LOGIN] Usuario: {correo} - Contraseña: {contra}")
        messagebox.showinfo("Inicio de sesión", "Sesión iniciada (simulada)")

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()