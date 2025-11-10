import sqlite3
from datetime import date
from dominio.entidades.usuario import Usuario

class UsuariosRepo:
    def __init__(self, db_path: str = "datos/app.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def crear(self, usuario: Usuario) -> int:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO usuarios (nombre, correo, contraseña_hash, fecha_creacion, estado)
                VALUES (?, ?, ?, ?, ?)
            """, (
                usuario.nombre,
                usuario.correo,
                usuario.contrasenia,
                usuario.fecha_creacion.isoformat(),
                usuario.estado.value
            ))
            conn.commit()
            return cur.lastrowid

    def obtener_por_correo(self, correo: str, contrasenia: str) -> Usuario | None:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT *
                FROM usuarios
                WHERE correo = ? AND contraseña_hash = ?
            """, (correo,contrasenia))
            row = cur.fetchone()

        if row:
            return Usuario(
                id=row[0],
                nombre=row[1],
                correo=row[2],
                contrasenia=row[3],
                fecha_creacion=date.fromisoformat(row[4]),
                estado=row[5]
            )
        return None