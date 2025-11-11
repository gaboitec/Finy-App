import sqlite3
from datetime import date
from dominio.entidades.transaccion import Transaccion
from dominio.objetos_valor.metodo_transaccion import MetodoTransaccion
from dominio.objetos_valor.tipo_transaccion import TipoTransaccion

class TransactionsRepo:
    def __init__(self, db_path: str = "datos/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, tx: Transaccion) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO transacciones (id_usuario, id_categoria, tipo, fecha, cantidad, descripcion, metodo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                tx.id_usuario,
                tx.id_categoria,
                tx.tipo.value,
                tx.fecha.isoformat(),
                tx.cantidad,
                tx.descripcion,
                tx.metodo.value
            ))
            conn.commit()
            return cur.lastrowid

    def obtener_por_usuario(self, id_usuario: int) -> list[Transaccion]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT t.id, t.id_usuario, t.id_categoria, t.tipo, t.fecha, t.cantidad, t.descripcion, t.metodo, c.nombre
                FROM transacciones AS t
                INNER JOIN categorias AS c
                    ON t.id_usuario = c.id_usuario AND t.id_categoria = c.id
                WHERE t.id_usuario = ?
                ORDER BY t.fecha DESC
            """, (id_usuario,))
            rows = cur.fetchall()

        return [
            Transaccion(
                id=row[0],
                id_usuario=row[1],
                id_categoria=row[2],
                tipo=TipoTransaccion(row[3]),
                fecha=row[4],
                cantidad=row[5],
                descripcion=row[6],
                metodo=MetodoTransaccion(row[7]),
                categoria=row[8]
            )
            for row in rows
        ]