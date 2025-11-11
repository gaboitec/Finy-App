import tkinter as tk
from tkinter import ttk

class TablaRegistros(tk.Frame):
    def __init__(self, master, columnas: list[str]):
        super().__init__(master)
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def limpiar(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def agregar_fila(self, valores: list[str]):
        self.tree.insert("", "end", values=valores)