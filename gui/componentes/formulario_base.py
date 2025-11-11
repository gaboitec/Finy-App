import tkinter as tk

class FormularioBase(tk.Toplevel):
    def __init__(self, master, titulo="Formulario"):
        super().__init__(master)
        self.title(titulo)
        self.geometry("400x500")
        self.configure(bg="white")
        self.campos = {}

    def agregar_campo(self, etiqueta: str, tipo="entry", opciones=None):
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="x", pady=5, padx=10)

        tk.Label(frame, text=etiqueta + ":", bg="white").pack(anchor="w")

        if tipo == "entry":
            entrada = tk.Entry(frame)
            entrada.pack(fill="x")
        elif tipo == "combo":
            entrada = tk.StringVar()
            combo = tk.OptionMenu(frame, entrada, *opciones)
            combo.pack(fill="x")
            entrada = entrada
        else:
            raise ValueError("Tipo de campo no soportado")

        self.campos[etiqueta] = entrada

    def obtener_valores(self) -> dict[str, str]:
        valores = {}
        for etiqueta, widget in self.campos.items():
            if isinstance(widget, tk.Entry):
                valores[etiqueta] = widget.get().strip()
            elif isinstance(widget, tk.StringVar):
                valores[etiqueta] = widget.get().strip()
        return valores