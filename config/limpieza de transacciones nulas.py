import sqlite3

with sqlite3.connect("../datos/app.db") as conn:
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM transacciones WHERE metodo IS NULL;
    """)

    cur.execute("""
        DELETE FROM categorias WHERE nombre = '1';
    """)

    conn.commit()