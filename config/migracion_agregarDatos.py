import sqlite3

with sqlite3.connect("../datos/app.db") as conn:
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO categorias 
        VALUES (1, 1, 'Ocio');
    """)

    cur.execute("""
        INSERT INTO deudas
        VALUES (1, 1, '2024-01-01', '2024-06-01','2025-01-01', 5000.0, 5.0, 'Préstamo personal', 'pendiente');
    """)

    cur.execute("""
        INSERT INTO deudores
        VALUES (1, 1, 'Juan Pérez', '53535353', 2000.0, '2024-02-01', '2024-12-01', 'pendiente');
    """)

    cur.execute("""
        INSERT INTO presupuestos
        VALUES (1, 1, 1, '2024-01-01', '2024-01-31', 300.0, 'activo');
    """)

    cur.execute("""
        INSERT INTO transacciones
        VALUES (1, 1, 1, 'gasto', '2024-01-15', 50.0, 'Compra de libros', 'efectivo');
    """)

    conn.commit()