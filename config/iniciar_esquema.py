import sqlite3
import os

def crear_esquema(db_path="../datos/app.db", esquema_path="../config/esquema.sql"):
    print("Creando...")
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        with open(esquema_path, "r", encoding="utf-8") as f:
            cur.executescript(f.read())
    print("Exito.")

crear_esquema()