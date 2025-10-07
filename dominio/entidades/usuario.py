from dataclasses import dataclass
from datetime import datetime
from dominio.objetos_valor.estado_usuario import Estado

@dataclass
class Usuario:
    id: int | None
    nombre: str
    correo: str
    contrasenia: str
    fecha_creacion: datetime
    estado: Estado = Estado.ACTIVO