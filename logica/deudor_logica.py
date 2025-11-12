from dominio.entidades.deudor import Deudor
from dominio.objetos_valor.estado_deuda import EstadoDeuda
from gestores.deudores_gestor import DeudoresRepo
from datetime import date

class DeudorService:
    def __init__(self, repo: DeudoresRepo):
        self.repo = repo

    def registrar_deudor(self, deudor):
        return self.repo.crear(deudor)

    def listar_por_usuario(self, id_usuario: int) -> list[Deudor]:
        try:
            return self.repo.obtener_por_usuario(id_usuario)
        except Exception as e:
            print(f"Error al obtener datos para usuario {id_usuario}: {e}")
            return []

    def total_por_estado(self, id_usuario: int, estado: EstadoDeuda) -> float:
        try:
            deudores = self.repo.obtener_por_usuario(id_usuario)
            return sum(d.cantidad for d in deudores if d.estado == estado)
        except Exception as e:
            print(f"Error al obtener datos para usuario {id_usuario}: {e}")
            return 0.0

    def listar_por_estado(self, id_usuario: int, estado: EstadoDeuda) -> list[Deudor]:
        try:
            return [d for d in self.repo.obtener_por_usuario(id_usuario) if d.estado == estado]
        except Exception as e:
            print(f"Error al obtener datos para usuario {id_usuario}: {e}")
            return []