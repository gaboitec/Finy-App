# archivo: poblar_datos.py

import sqlite3
from datetime import datetime

DB_PATH = "../datos/app.db"

with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()

    # Limpiar registros anteriores de prueba
    cur.execute("DELETE FROM transacciones WHERE descripcion LIKE 'Ejemplo %';")
    cur.execute("DELETE FROM categorias WHERE nombre LIKE 'Ejemplo %';")

    # Insertar categorías de ejemplo
    categorias = ["Ejemplo Alimentación", "Ejemplo Transporte", "Ejemplo Entretenimiento", "Ejemplo Ingreso", "Ejemplo Salud"]
    categoria_ids = []

    for nombre in categorias:
        cur.execute("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))
        categoria_ids.append(cur.lastrowid)

    # Insertar transacciones de ejemplo
    hoy = datetime.now().date().isoformat()
    transacciones = [
        (1, "gasto", categoria_ids[0], 150.00, "Ejemplo 1", hoy),
        (1, "gasto", categoria_ids[1], 60.00, "Ejemplo 2", hoy),
        (1, "gasto", categoria_ids[2], 120.00, "Ejemplo 3", hoy),
        (1, "ingreso", categoria_ids[3], 1000.00, "Ejemplo 4", hoy),
        (1, "gasto", categoria_ids[4], 80.00, "Ejemplo 5", hoy),
    ]

    cur.executemany("""
        INSERT INTO transacciones (id_usuario, tipo, id_categoria, cantidad, descripcion, fecha)
        VALUES (?, ?, ?, ?, ?, ?)
    """, transacciones)

    conn.commit()

print("Datos de ejemplo insertados correctamente.")
