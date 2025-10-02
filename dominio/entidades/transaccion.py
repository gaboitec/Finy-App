from dataclasses import dataclass
from datetime import datetime
from dominio.objetos_valor.tipo_transaccion import TipoTransaccion
from dominio.objetos_valor.metodo_transaccion import MetodoTransaccion

@dataclass
class Transaccion:
    id: int | None
    id_usuario: int
    id_categoria: int
    tipo: TipoTransaccion
    fecha: datetime
    cantidad: float
    descripcion: str
    metodo: MetodoTransaccion

