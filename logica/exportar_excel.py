import openpyxl
from openpyxl.styles import Font
from tkinter import filedialog, messagebox
import os

def exportar_excel(treeview, nombre_archivo="exportado.xlsx"):
    # Diálogo para guardar
    ruta = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        initialfile=nombre_archivo
    )

    if not ruta:
        return  # Usuario canceló

    # Verificar si el archivo ya existe
    if os.path.exists(ruta):
        respuesta = messagebox.askyesno(
            "Archivo existente",
            f"El archivo '{os.path.basename(ruta)}' ya existe.\n¿Deseas sobrescribirlo?"
        )
        if not respuesta:
            return  # Usuario no quiere sobrescribir

    # Crear libro
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Datos"

    # Encabezados
    columnas = [treeview.heading(col)["text"] for col in treeview["columns"]]
    ws.append(columnas)

    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Filas
    for item in treeview.get_children():
        valores = treeview.item(item)["values"]
        ws.append(valores)

    # Guardar
    try:
        wb.save(ruta)
        messagebox.showinfo("Exportación exitosa", f"Archivo guardado en:\n{ruta}")
    except Exception as e:
        messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo:\n{e}")
