from dominio.entidades.presupuesto import Presupuesto
from dominio.objetos_valor.estado_presupuesto import EstadoPresupuesto
from gestores.presupuestos_gestor import PresupuestosRepo
from datetime import date

class PresupuestoService:
    def __init__(self, repo: PresupuestosRepo):
        self.repo = repo

    def crear_presupuesto(self, id_usuario: int, fecha_inicio: date, fecha_fin: date, cantidad: float, id_categoria: int | None = None) -> int:
        presupuesto = Presupuesto(
            id=None,
            id_usuario=id_usuario,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            cantidad=cantidad,
            id_categoria=id_categoria,
            estado=EstadoPresupuesto.ACTIVO
        )
        return self.repo.crear(presupuesto)

    def listar_presupuestos(self, id_usuario: int) -> list[Presupuesto]:
        return self.repo.obtener_por_usuario(id_usuario)