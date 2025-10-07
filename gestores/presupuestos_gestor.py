# app/repositories/presupuestos_repo.py

import sqlite3
from datetime import date
from dominio.entidades.presupuesto import Presupuesto
from dominio.objetos_valor.estado_presupuesto import EstadoPresupuesto

class PresupuestosRepo:
    def __init__(self, db_path: str = "data/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, presupuesto: Presupuesto) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO presupuestos (id_usuario, id_categoria, fecha_inicio, fecha_fin, cantidad, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                presupuesto.id_usuario,
                presupuesto.id_categoria,
                presupuesto.fecha_inicio.isoformat(),
                presupuesto.fecha_fin.isoformat(),
                presupuesto.cantidad,
                presupuesto.estado.value
            ))
            conn.commit()
            return cur.lastrowid

    def obtener_por_usuario(self, id_usuario: int) -> list[Presupuesto]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, id_usuario, fecha_inicio, fecha_fin, cantidad, id_categoria, estado
                FROM presupuestos
                WHERE id_usuario = ?
                ORDER BY fecha_inicio DESC
            """, (id_usuario,))
            rows = cur.fetchall()

        return [
            Presupuesto(
                id=row[0],
                id_usuario=row[1],
                fecha_inicio=date.fromisoformat(row[2]),
                fecha_fin=date.fromisoformat(row[3]),
                cantidad=row[4],
                id_categoria=row[5],
                estado=EstadoPresupuesto(row[6])
            )
            for row in rows
        ]