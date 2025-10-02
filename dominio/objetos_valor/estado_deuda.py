from enum import Enum

class EstadoDeuda(Enum):
    PENDIENTE = "pendiente"
    PAGADA = "pagada"
    ATRASADA = "atrasada"
    ACTIVA = "activa"


