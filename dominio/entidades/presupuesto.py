from dataclasses import dataclass
from datetime import date
from dominio.objetos_valor.estado_presupuesto import EstadoPresupuesto

@dataclass
class Presupuesto:
    id: int | None
    id_usuario: int
    fecha_inicio: date
    fecha_fin: date
    cantidad: float
    id_categoria: int | None = None  # opcional
    estado: EstadoPresupuesto = EstadoPresupuesto.ACTIVO
