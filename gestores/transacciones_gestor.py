import sqlite3
from datetime import datetime
from dominio.entidades.transaccion import Transaccion
from dominio.objetos_valor.metodo_transaccion import MetodoTransaccion
from dominio.objetos_valor.tipo_transaccion import TipoTransaccion

class TransactionsRepo:
    def __init__(self, db_path: str = "data/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, tx: Transaccion) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO transacciones (id_usuario, id_categoria, tipo, cantidad, descripcion, fecha)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                tx.id_usuario,
                tx.id_categoria,
                tx.tipo.value,
                tx.cantidad,
                tx.descripcion,
                tx.fecha.isoformat()
            ))
            conn.commit()
            return cur.lastrowid

    def obtener_por_usuario(self, id_usuario: int) -> list[Transaccion]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, id_usuario, id_categoria, tipo, cantidad, descripcion, fecha
                FROM transacciones
                WHERE id_usuario = ?
                ORDER BY fecha DESC
            """, (id_usuario,))
            rows = cur.fetchall()

        return [
            Transaccion(
                id=row[0],
                id_usuario=row[1],
                id_categoria=row[2],
                tipo=TipoTransaccion(row[3]),
                fecha=datetime.fromisoformat(row[6]),
                cantidad=row[4],
                descripcion=row[5],
                metodo=MetodoTransaccion(row[7])
            )
            for row in rows
        ]