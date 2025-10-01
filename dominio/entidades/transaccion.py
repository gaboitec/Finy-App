from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TipoTransaccion(Enum):
    INGRESO = "ingreso"
    GASTO = "gasto"

@dataclass
class Transaccion:
    id: int | None
    id_usuario: int
    id_categoria: int
    tipo: TipoTransaccion
    cantidad: float
    descripcion: str
    fecha: datetime
