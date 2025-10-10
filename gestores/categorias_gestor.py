import sqlite3
from dominio.entidades.categoria import Categoria

class CategoriasRepo:
    def __init__(self, db_path: str = "data/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, categoria: Categoria) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO categorias (id_usuario, nombre)
                VALUES (?, ?)
            """, (categoria.id_usuario, categoria.nombre))
            conn.commit()
            return cur.lastrowid

    def obtener_por_usuario(self, id_usuario: int) -> list[Categoria]:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, id_usuario, nombre
                FROM categorias
                WHERE id_usuario = ?
                ORDER BY nombre ASC
            """, (id_usuario,))
            rows = cur.fetchall()

        return [
            Categoria(id=row[0], id_usuario=row[1], nombre=row[2])
            for row in rows
        ]