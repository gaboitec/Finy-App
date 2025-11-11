import tkinter as tk

class EncabezadoBotones(tk.Frame):
    def __init__(self, master, on_nuevo, on_exportar_pdf=None, on_exportar_excel=None):
        super().__init__(master, bg="white")

        btn_nuevo = tk.Button(self, text="Agregar nuevo", bg="#4CAF50", fg="white", command=on_nuevo)
        btn_nuevo.pack(side="left", padx=5)

        if on_exportar_pdf:
            btn_pdf = tk.Button(self, text="Exportar PDF", command=on_exportar_pdf)
            btn_pdf.pack(side="left", padx=5)

        if on_exportar_excel:
            btn_excel = tk.Button(self, text="Exportar Excel", command=on_exportar_excel)
            btn_excel.pack(side="left", padx=5)