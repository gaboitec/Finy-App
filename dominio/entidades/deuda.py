from dataclasses import dataclass
from datetime import date
from dominio.objetos_valor.estado_deuda import EstadoDeuda

@dataclass
class Deuda:
    id: int | None
    id_usuario: int
    plazo_inicio: date
    plazo_fin: date
    cantidad: float
    interes: float
    descripcion: str
    estado: EstadoDeuda = EstadoDeuda.PENDIENTE
