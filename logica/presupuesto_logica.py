from dominio.entidades.presupuesto import Presupuesto
from dominio.objetos_valor.estado_presupuesto import EstadoPresupuesto
from gestores.presupuestos_gestor import PresupuestosRepo
from gestores.categorias_gestor import CategoriasRepo
from logica.categoria_logica import CategoriaService
from datetime import date

class PresupuestoService:
    def __init__(self, repo: PresupuestosRepo):
        self.repo = repo

    def crear_presupuesto(self, id_usuario: int, fecha_inicio: date, fecha_fin: date, cantidad: float, id_categoria: int | None = None) -> int:
        categoria = CategoriaService(CategoriasRepo()).buscar_por_nombre(id_usuario, id_categoria)
        presupuesto = Presupuesto(
            id=None,
            id_usuario=id_usuario,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            cantidad=cantidad,
            id_categoria=categoria,
            estado=EstadoPresupuesto("activo")
        )
        return self.repo.crear(presupuesto)

    def listar_presupuestos(self, id_usuario: int) -> list[Presupuesto]:
        try:
            return self.repo.obtener_por_usuario(id_usuario)
        except Exception as e:
            print(f"Error al obtener datos para usuario {id_usuario}: {e}")
            return []