import sqlite3
from dominio.entidades.deuda import Deuda
from dominio.objetos_valor.estado_deuda import  EstadoDeuda
from datetime import date

class DeudasRepo:
    def __init__(self, db_path: str = "data/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, deuda: Deuda) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO deudas (id_usuario, plazo_inicio, plazo_fin, cantidad, interes, descripcion, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                deuda.id_usuario,
                deuda.plazo_inicio.isoformat(),
                deuda.plazo_fin.isoformat(),
                deuda.cantidad,
                deuda.interes,
                deuda.descripcion,
                deuda.estado.value
            ))
            conn.commit()
            return cur.lastrowid

    def obtener_por_usuario(self, id_usuario: int) -> list[Deuda]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, id_usuario, plazo_inicio, plazo_fin, cantidad, interes, descripcion, estado
                FROM deudas
                WHERE id_usuario = ?
                ORDER BY plazo_fin ASC
            """, (id_usuario,))
            rows = cur.fetchall()

        return [
            Deuda(
                id=row[0],
                id_usuario=row[1],
                plazo_inicio=date.fromisoformat(row[2]),
                plazo_fin=date.fromisoformat(row[3]),
                cantidad=row[4],
                interes=row[5],
                descripcion=row[6],
                estado=EstadoDeuda(row[7])
            )
            for row in rows
        ]