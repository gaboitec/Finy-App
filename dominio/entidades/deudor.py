from dataclasses import dataclass
from datetime import date
from dominio.objetos_valor.estado_deuda import EstadoDeuda

@dataclass
class Deudor:
    id: int | None
    id_usuario: int
    nombre: str
    contacto: str
    cantidad: float
    plazo_inicio: date
    plazo_fin: date
    estado: EstadoDeuda = EstadoDeuda.ACTIVA
