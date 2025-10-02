from enum import Enum

class MetodoTransaccion(Enum):
    EFECTIVO = "efectivo"
    TARJETA = "tarjeta"
    TRANSFERENCIA = "transferencia"
    OTRO = "otro"
