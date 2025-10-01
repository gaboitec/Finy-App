-- Activar claves foraneas en SQLite
PRAGMA foreign_keys = ON;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contraseña_hash TEXT NOT NULL,
    fecha_creacion DATE DEFAULT CURRENT_DATE,
    estado TEXT DEFAULT 'activo'
);

-- Tabla de categorías (para cada usuario)
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

-- Tabla de transacciones
CREATE TABLE IF NOT EXISTS transacciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    tipo TEXT CHECK(tipo IN ('ingreso', 'gasto')) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    cantidad REAL NOT NULL,
    descripcion TEXT,
    metodo TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

-- Tabla de presupuestos
CREATE TABLE IF NOT EXISTS presupuestos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_categoria INTEGER, -- opcional
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    cantidad REAL NOT NULL,
    estado TEXT DEFAULT 'activo',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

-- Tabla de deudas
CREATE TABLE IF NOT EXISTS deudas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    plazo_inicio DATE NOT NULL,
    plazo_fin DATE NOT NULL,
    fecha_pago DATE,
    cantidad REAL NOT NULL,
    interes REAL DEFAULT 0,
    descripcion TEXT,
    estado TEXT DEFAULT 'pendiente',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

-- Tabla de deudores
CREATE TABLE IF NOT EXISTS deudores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    contacto TEXT,
    cantidad REAL NOT NULL,
    plazo_inicio DATE NOT NULL,
    plazo_fin DATE NOT NULL,
    estado TEXT DEFAULT 'activo',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);
