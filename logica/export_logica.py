import pandas as pd
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
#from datetime import datetime

class ExportService:
    def exportar_csv(self, datos: list[dict], nombre_archivo: str) -> str:
        df = pd.DataFrame(datos)
        ruta = f"export/{nombre_archivo}.csv"
        df.to_csv(ruta, index=False)
        return ruta

    def exportar_excel(self, datos: list[dict], nombre_archivo: str) -> str:
        df = pd.DataFrame(datos)
        ruta = f"export/{nombre_archivo}.xlsx"
        df.to_excel(ruta, index=False)
        return ruta

    def exportar_pdf(self, datos: list[dict], nombre_archivo: str, titulo: str = "Reporte"):
        ruta = f"export/{nombre_archivo}.pdf"
        c = canvas.Canvas(ruta, pagesize=LETTER)
        width, height = LETTER

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, titulo)

        c.setFont("Helvetica", 10)
        y = height - 80
        for i, fila in enumerate(datos):
            texto = ", ".join(f"{k}: {v}" for k, v in fila.items())
            c.drawString(50, y, texto)
            y -= 15
            if y < 50:
                c.showPage()
                y = height - 50

        c.save()
        return ruta