from app.servicios.export_service import ExportService

datos = [
    {"Fecha": "2025-10-01", "Tipo": "Gasto", "Cantidad": 150.0, "Categoría": "Comida"},
    {"Fecha": "2025-10-02", "Tipo": "Ingreso", "Cantidad": 500.0, "Categoría": "Salario"}
]

export = ExportService()
csv_path = export.exportar_csv(datos, "transacciones_octubre")
excel_path = export.exportar_excel(datos, "transacciones_octubre")
pdf_path = export.exportar_pdf(datos, "transacciones_octubre", titulo="Transacciones Octubre")

print("Archivos generados:")
print(csv_path)
print(excel_path)
print(pdf_path)