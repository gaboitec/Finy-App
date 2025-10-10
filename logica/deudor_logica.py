from dominio.entidades.deudor import Deudor
from dominio.objetos_valor.estado_deuda import EstadoDeuda
from gestores.deudores_gestor import DeudoresRepo
from datetime import date

class DeudorService:
    def __init__(self, repo: DeudoresRepo):
        self.repo = repo

    def registrar_deudor(self, id_usuario: int, nombre: str, contacto: str, cantidad: float, plazo_inicio: date, plazo_fin: date) -> int:
        deudor = Deudor(
            id=None,
            id_usuario=id_usuario,
            nombre=nombre,
            contacto=contacto,
            cantidad=cantidad,
            plazo_inicio=plazo_inicio,
            plazo_fin=plazo_fin,
            estado=EstadoDeuda.ACTIVA
        )
        return self.repo.crear(deudor)

    def listar_por_usuario(self, id_usuario: int) -> list[Deudor]:
        return self.repo.obtener_por_usuario(id_usuario)

    def total_por_estado(self, id_usuario: int, estado: EstadoDeudor) -> float:
        deudores = self.repo.obtener_por_usuario(id_usuario)
        return sum(d.cantidad for d in deudores if d.estado == estado)

    def listar_por_estado(self, id_usuario: int, estado: EstadoDeudor) -> list[Deudor]:
        return [d for d in self.repo.obtener_por_usuario(id_usuario) if d.estado == estado]