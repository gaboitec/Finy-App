import sqlite3
from dominio.entidades.deudor import Deudor
from dominio.objetos_valor.estado_deuda import  EstadoDeuda
from datetime import date

class DeudoresRepo:
    def __init__(self, db_path: str = "datos/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, deudor: Deudor) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO deudores (id_usuario, nombre, contacto, cantidad, plazo_inicio, plazo_fin, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                deudor.id_usuario,
                deudor.nombre,
                deudor.contacto,
                deudor.cantidad,
                deudor.plazo_inicio.isoformat(),
                deudor.plazo_fin.isoformat(),
                deudor.estado.value
            ))
            conn.commit()
            return cur.lastrowid

    def obtener_por_usuario(self, id_usuario: int) -> list[Deudor]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, id_usuario, nombre, contacto, cantidad, plazo_inicio, plazo_fin, estado
                FROM deudores
                WHERE id_usuario = ?
                ORDER BY plazo_fin ASC
            """, (id_usuario,))
            rows = cur.fetchall()

        return [
            Deudor(
                id=row[0],
                id_usuario=row[1],
                nombre=row[2],
                contacto=row[3],
                cantidad=row[4],
                plazo_inicio=row[5],
                plazo_fin=row[6],
                estado=EstadoDeuda(row[7])
            )
            for row in rows
        ]